from fastapi import APIRouter
from schemas.users import user_lists
from models.user import User, UpdateUser
from db.config import collection
router = APIRouter(prefix="/api/v1", tags=["Creating User, Updating user and Authentication"])

@router.get("/get_user")
async def get_user():
    users = collection.find()
    return user_lists(users)

@router.post("/post_user")
async def add_user(user: User):
    collection.insert_one(user.model_dump())
    return {"message": "User added sucessfully"}
