import email
from email.policy import default
from msilib import Table
from pydantic import BaseModel
#from typing import List,Optional
#from sqlmodel import Field,Column,SQLModel,JSON



# class Event(SQLModel,Table=True):
#     id: int = Field(default=None,primary_key=True)
#     title: str
#     image: str
#     description: str
#     tags: List[str] =Field(sa_column =Column(JSON))
#     location: str
#     # class Config:
#      #arbitrary_types_allowed = True
#     #         schema_extra = {
#     #         "example": {
#     #         "title": "FastAPI Book Launch",
#     #         "image": "https://linktomyimage.com/image.png",
#     #         "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
#     #         "tags": ["python", "fastapi", "book", 
#     #         "launch"],
#     #         "location": "Google Meet"
#     #         }
#     #         }
# class EventUpdate(SQLModel):
#     title: Optional[str]
#     image: Optional[str]
#     description: Optional[str]
#     tags: Optional[List[str]]
#     location: Optional[str]
from beanie import Document
from typing import Optional, List

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        name = "events"

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]