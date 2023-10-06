from os import name
import uvicorn
import os
from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from db import models
from db.database import engine
from routers import user, post, comment, partner
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

app.include_router(user.router)
# app.include_router(post.router)
# app.include_router(comment.router)
app.include_router(authentication.router)
app.include_router(partner.router)


@app.get("/")
def root():
  return "Hello world!"


origins = [
  'http://localhost:3000',
  'http://localhost:3001',
  'http://localhost:3002',
  '*'
]

# config middleware 
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')



if __name__ == "__main__":
  uvicorn.run(app="main:app", host="0.0.0.0", port=8002, log_level="info", reload=True  )
