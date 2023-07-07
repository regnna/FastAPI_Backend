from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,Response,HTTPException
# from fastapi import Response
# from ... 
import models
# from ... 
import schemas

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"done"}

def update(id,request:schemas.Blog,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
    blog.update(request.dict())
    db.commit()
    return "updated"


def showIdBlog(id,response:Response,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,detail=f"blog with the id {id} not available")
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"details":f"blog with the id {id} not available"}
    return blog   
