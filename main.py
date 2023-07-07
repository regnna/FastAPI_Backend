from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
    

@app.get('/blog')          #('/')= path get= operation @app= path operation decorator
def index(limit=10,published:bool=True,sort:Optional[str]=None):           #Path operation funxtion
    #only get 10 published blogs
    #limit is a query parameter
    if published:
        return {"data":f"{limit} published blogs from the db "}
    return {"data":f"{limit} unpublished blogs from the db "}
    

@app.get("/about")
def about():
    return {"data":{"about Page"}}

@app.get("/docs")
def uverlap():
    return "is the swagger ui is working? "

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')   # id is a path parameter
def show(id: int):
    #fetch blog with id = id
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id =id
    return {'data':{'1','2'}}

@app.post('/blog')
def create_blog(request:Blog ):
    # return request
    return {"data":f"Blog is created with title: {request.title}"}

# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port="9000")