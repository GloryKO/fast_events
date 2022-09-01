# from sqlmodel import SQLModel,Session,create_engine
# from models.events import Event
# database_file = "planner.db"
# database_connection_string = f"sqlite:///{database_file}"
# connect_args = {"check_same_thread": False}
# engine_url = create_engine(database_connection_string, 
# echo=True, connect_args=connect_args)

# def conn():
#     SQLModel.metadata.create_all(engine_url)

# def get_session():
#     with Session(engine_url) as session:
#         yield session

from unittest.mock import Base
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings,BaseModel
from models.users import User 
from models.events import Event
from typing import Any, List, Optional

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] =None
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),document_models=[Event,User])
    
    class Config:
        env_file = ".env"

class Database:
        def __init__(self, model):
            self.model = model

        async def save(self,document):
            await document.create()
            return 
        
        async def get(self,id:PydanticObjectId):
            doc = await self.model.get(id)
            if doc :
                return doc 
            return False
        
        async def get_all(self):
            doc = await self.model.find_all()
            return doc 
        
        async def update(self,id:PydanticObjectId,body:BaseModel):
            doc_id =id
            des_body = body.dict()
            update_query = {"$set":{k:v for k,v in des_body.items() if v is not None }}
            doc =await self.get(doc_id)
            if not doc:
                return False
            await doc.update(update_query) 
        
        async def delete(self,id:PydanticObjectId):
            doc_id = await self.get(id)
            if not doc_id:
                return False
            await self.delete(doc_id)
            return True
            

