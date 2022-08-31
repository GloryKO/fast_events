import email
from pydantic import BaseModel,EmailStr
from typing import List
from typing import Optional,List
from models.events import Event
from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event

# class User(BaseModel):
#     email: EmailStr
#     password: str
#     events: Optional[List[Event]]
#     class Config:
#         schema_extra = {
#         "example": {
#         "email": "fastapi@packt.com",
#         "username": "strong!!!",
#         "events": [],
#         }
#         }
class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]
    class Settings:
        name = "users"

class UserSignIn(BaseModel):
    email: EmailStr
    password : str
    # class Config:
    #     schema_extra = {
    #     "example": {
    #     "email": "fastapi@packt.com",
    #     "password": "strong!!!",
    #     "events": [],
    #     }
    #     }


