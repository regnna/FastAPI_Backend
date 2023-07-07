from fastapi import APIRouter,Depends,HTTPException,status
# from ..schemas 
from schemas import *
# import Login
# from ..database 
# import get_db
from database import *
import models
from hashing import Hash
from tokin import create_access_token
# from .. import database
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
# from jose import jwt,JWTError
# import sys
# sys.setrecursionlimit(10000)

router=APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request:Login,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Creadentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect Password")
    # return user
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}