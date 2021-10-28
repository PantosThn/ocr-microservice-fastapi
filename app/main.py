import pathlib
import os
import io
from functools import lru_cache
import uuid
from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
    Request,
    File,
    UploadFile
    )
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings

#this env file is used for debug purposes
class Settings(BaseSettings):
    debug: bool = False
    echo_active: bool = False
    class Config:
        env_file = ".env"

#with the decorator below this function is called only once
@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
DEBUG = settings.debug

BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

#Rest API
@app.get("/", response_class=HTMLResponse) # http GET -> JSON
def home_view(request: Request, settings:Settings = Depends(get_settings)):
    #i have to declare the request task above
    #ussing HTMLResponse to bring back a string(html) and not a json.
    #FastAPI always returns a json unless changes are made
    #jinja2 converts html files like python's format.The idea is to take those files and return them as string
    return templates.TemplateResponse("home.html", {"request": request, "name": "Thanos"})

@app.post("/")
def home_detail_view():
    return {"hello": "world"}

@app.post("/img-echo/", response_class=FileResponse) #http post
async def img_echo_view(file:UploadFile = File(...), settings:Settings = Depends(get_settings)):
    if not settings.echo_active:
        raise HTTPException(detail="Invalid endpoint", status_code=400)
    bytes_str =  io.BytesIO(await file.read()) #read image as a byte stream
    fname = pathlib.Path(file.filename)
    fext = fname.suffix #.jpg
    #use uuid1 which contaings a timestamp for file naming
    dest = UPLOAD_DIR / f"{uuid.uuid1}{fext}"
    with open(str(dest), 'wb') as out:
        out.write(bytes_str.read())
    return dest
