from fastapi import APIRouter,HTTPException, status
from models.users import User , UserSignIn

user_router = APIRouter (
   tags = ["User"]
)

users ={}

@user_router.post("/signup")
async def sign_new_user(data: User)-> dict:
    if data.email in users:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with name already exists"

        )
    users[data.email] = data
    return {
        "Message":"User Successfully registered"
    }


@user_router.post("/signin")
async def sign_user_in(user:UserSignIn)-> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User does not exists"
        )
    if users[user.password] != user.password:
        raise HTTPException(
            status_code = status.HTTP_401_FORBIDDEN,
            detail = "Wrong credentials provided"

        )
    return {
        "Message":"User Successfully Signed in"
    }