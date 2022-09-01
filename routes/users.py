from fastapi import APIRouter,HTTPException, status
from models.users import User , UserSignIn
from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event
from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSignIn
user_router = APIRouter(
 tags=["User"],
)
user_database = Database(User)

user_router = APIRouter (
   tags = ["User"]
)

# users ={}

# @user_router.post("/signup")
# async def sign_new_user(data: User)-> dict:
#     if data.email in users:
#         raise HTTPException(
#             status_code = status.HTTP_409_CONFLICT,
#             detail = "User with name already exists"

#         )
#     users[data.email] = data
#     return {
#         "Message":"User Successfully registered"
#     }


# @user_router.post("/signin")
# async def sign_user_in(user:UserSignIn)-> dict:
#     if users[user.email] not in users:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND,
#             detail = "User does not exists"
#         )
#     if users[user.password] != user.password:
#         raise HTTPException(
#             status_code = status.HTTP_401_FORBIDDEN,
#             detail = "Wrong credentials provided"

#         )
#     return {
#         "Message":"User Successfully Signed in"
#     }

@user_router.post("/signup")
async def sign_user_up(user:User):
    user_exist = await User.find_one(User.email==user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
            )
    await user_database.save(user)
    return { "message": "User created successfully"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    user_exist = await User.find_one(User.email == 
    user.email)
    if not user_exist:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User with email does not exist."
        )
    if user_exist.password == user.password:
        return {
        "message": "User signed in successfully."
        }
    raise HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid details passed."
    )