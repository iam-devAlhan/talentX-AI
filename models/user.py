from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    hashed_password: str
    created_at: float = datetime.timestamp(datetime.now())

class UpdateUser(BaseModel):
    name: Optional[str] = None
    hashed_password: Optional[str] = None