from typing import List
from fastapi import APIRouter,Depends,status,Response,HTTPException
# from .. 
import schemas
from sqlalchemy.orm import Session
from database import get_db
import database
# from .. 
import models
from .repository import user

router=APIRouter(
    prefix="/user",
    tags=['users']
)

get_db = database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user.create_userr(request,db)
        # new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
        # db.add(new_user)
        # db.commit()
        # db.refresh(new_user)

        # return new_user



@router.get('/',response_model=List[schemas.ShowUser])
def all_user(db:Session=Depends(get_db)):
    # return db.query(models.User).all()
    return user.alll_users(db)

@router.get('/{id}',response_model=schemas.ShowUser)
def show_user(id,db:Session=Depends(get_db)):
    fetched_user=db.query(models.User).filter(models.User.id==id).first()
    if not fetched_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} not available using HTTPException")
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"details":f"User with the id {id} not available"}
    return fetched_user
