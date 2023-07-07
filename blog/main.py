from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
import uvicorn
import models,schemas
 
# from .hashing import Hash
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from routers import blog,users,authentication
# from . import schemas,models

# from Response import response

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)

app.include_router(blog.router)

app.include_router(users.router)

# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create(request: schemas.Blog,db: Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
#     # return request
#     # return {"title":title,"body":body}
#     # return "creating"

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
# def all(db: Session=Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
# def destroy(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {"done"}

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
# def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with the id {id} not available")
#     blog.update(request.dict())
#     db.commit()
#     return "updated"
#     # update(request)




# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])
# def show(id,response:Response,db:Session=Depends(get_db) ):
#     # Response response
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,detail=f"blog with the id {id} not available")
#         response.status_code=status.HTTP_404_NOT_FOUND
#         return {"details":f"blog with the id {id} not available"}
#     return blog




# @app.post('/user',response_model=schemas.ShowUser,tags=['users'])
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
#     new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user



# @app.get('/user',response_model=List[schemas.ShowUser],tags=['users'])
# def all_user(db:Session=Depends(get_db)):
#     return db.query(models.User).all()


# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
# def show_user(id,db:Session=Depends(get_db)):
#     fetched_user=db.query(models.User).filter(models.User.id==id).first()
#     if not fetched_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} not available using HTTPException")
#         response.status_code=status.HTTP_404_NOT_FOUND
#         return {"details":f"User with the id {id} not available"}
#     return fetched_user


# if __name__=="__main__":
    # uvicorn.run(app,host="127.0.0.1",port="9005")