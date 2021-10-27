import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
#Rest API

@app.get("/", response_class=HTMLResponse) # http GET -> JSON
def home_view(request: Request):
    #i have to declare the request task above
    #ussing HTMLResponse to bring back a string(html) and not a json.
    #FastAPI always returns a json unless changes are made
    #jinja2 converts html files like python's format.The idea is to take those files and return them as string
    return templates.TemplateResponse("home.html", {"request": request, "name": "Thanos"})

@app.post("/")
def home_detail_view():
    return {"hello": "world"}
