from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
import schemas
from sqlalchemy.orm import Session
from database import get_db
# from .. 
import models
from .repository import blog

router=APIRouter(
    prefix="/blog",
    tags=['blogs']
)



@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db)):
    return blog.get_all(db)

    # blogs=db.query(models.Blog).all()
    # return blogs


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db: Session=Depends(get_db)):
    return blog.create(request,db)
        # new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
        # db.add(new_blog)
        # db.commit()
        # db.refresh(new_blog)
        # return new_blog
    # return request
    # return {"title":title,"body":body}
    # return "creating"


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    return blog.delete(id,db)
        # blog=db.query(models.Blog).filter(models.Blog.id==id)
        # if not blog.first():
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
        # blog.delete(synchronize_session=False)
        # db.commit()
    # return {"done"}


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
        # blog=db.query(models.Blog).filter(models.Blog.id==id)
        # if not blog.first():
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
        # blog.update(request.dict())
        # db.commit()
        # return "updated"
    blog.update(id,request, db)
    # update(request) 


@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,response:Response,db:Session=Depends(get_db) ):
    return blog.showIdBlog(id, response, db)
    # Response response
        # blog=db.query(models.Blog).filter(models.Blog.id==id).first()
        # if not blog:
        #     raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,detail=f"blog with the id {id} not available")
        #     response.status_code=status.HTTP_404_NOT_FOUND
        #     return {"details":f"blog with the id {id} not available"}
        # return blog   