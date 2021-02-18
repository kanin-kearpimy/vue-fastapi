from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from dotenv import load_dotenv
# from app.modules.connect_database.ConnectDatabase import ConnectDatabase
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import os

# Basic Application Setup
app = FastAPI()
app.mount("/static", StaticFiles(directory='app/static'), name="static")
load_dotenv('./.env')

# Database Setup Start

# engine = create_engine('sqlite:///fastapi.db', echo=True)
# Base = declarative_base()
# class School(Base):

#     __tablename__ = "woot"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)  


#     def __init__(self, name):

#         self.name = name    

# if(os.path.isfile('fastapi.db') == False):
#     Base.metadata.create_all(engine)

# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('woot', metadata, autoload=True, autoload_with=engine)

# Database Setup End

# database = ConnectDatabase()

templates = Jinja2Templates(directory="app/template")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/api/add-list')
async def addList(request: Request):
    all_request = await request.json()
    return all_request