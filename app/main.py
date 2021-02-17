from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory='app/static'), name="static")

templates = Jinja2Templates(directory="app/template")

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})