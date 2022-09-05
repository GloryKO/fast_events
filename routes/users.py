from fastapi import APIRouter,HTTPException, status
from models.users import User
from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event
from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User
from auth.hashpassword import HashPassword
hash_password = HashPassword()
user_router = APIRouter(
 tags=["User"],
)
user_database = Database(User)

user_router = APIRouter (
   tags = ["User"]
)
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
from models.users import User
from models.users import User, TokenResponse
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
async def sign_user_up(user:OAuth2PasswordRequestForm = Depends()):
    user_exist = await User.find_one(User.email==user.username)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already."
            )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    if hash_password.verify_hash(user.password,user_exist.password):
        access_token = create_access_token(user_exist.email)
    return { 
        "access_token": access_token,
        "token_type": "Bearer"
    }

@user_router.post("/signin",response_model=TokenResponse)
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