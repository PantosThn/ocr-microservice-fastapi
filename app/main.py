import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # http GET -> JSON
def home_view():
    return {"hello": "world"}

@app.post("/")
def home_detail_view():
    return {"hello": "world"}