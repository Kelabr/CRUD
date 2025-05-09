from pydantic import BaseModel

class New_user(BaseModel):
    name:str
    email:str
    password:str

class Name(BaseModel):
    name:str
