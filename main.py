from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):

  # only gets 10 published blogs
  if published:
    return {'data': f'{limit} published blogs from the db'}
  else:
    return {'data': f'{limit} blogs from the db'}

@app.get('/about')
def about():
  return {'data': 'about page'}

class Blog(BaseModel):
  title: str
  body: str
  published: Optional[bool]

@app.post('/blog')
def create(blog: Blog):
  return blog