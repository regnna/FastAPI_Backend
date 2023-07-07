from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,Response,HTTPException
# from fastapi import Response
# from ... 
import models,hashing
# from ... 
import schemas

def create_userr(request:schemas.User,db:Session):
    new_user=models.User(name=request.name,email=request.email,password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def alll_users(db:Session):
    return db.query(models.User).all()


def showIdUser(id:int,db:Session):
    fetched_user=db.query(models.User).filter(models.User.id==id).first()
    if not fetched_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} not available using HTTPException")
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"details":f"User with the id {id} not available"}
    return fetched_user