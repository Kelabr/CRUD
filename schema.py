from pydantic import BaseModel

class New_user(BaseModel):
    name:str
    email:str
    password:str