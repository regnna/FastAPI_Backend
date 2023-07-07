from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class config():
        orm_mode=True



class UserBase(BaseModel):
    name:str
    email:str
    password:str

class User(UserBase):
    class config():
        orm_mode=True


class BlgUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class UsrBlog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode=True

class ShowUser(BaseModel):
    name:str
    email:str
    bloggs: List[UsrBlog]
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator: BlgUser
    class Config():
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str
    class Config():
        orm_mode=True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

# ShowBlog.update_forward_refs()
    
