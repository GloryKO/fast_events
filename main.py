from sys import prefix
from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
import uvicorn 
from database.connection import conn
from fastapi.middleware.cors import CORSMiddleware

origins =["*"]


app = FastAPI()
app.add_middleware(CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],)

app.include_router(user_router, prefix="/user")
app.include_router(event_router,prefix="/event")

@app.on_event("startup") #create a db connection on start of the app.
def on_startup():
    conn()


if __name__ == "__main__":
 uvicorn.run("main:app", reload=True)