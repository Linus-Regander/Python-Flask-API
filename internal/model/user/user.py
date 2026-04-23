from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum

class UserRole(Enum):
    ADMIN = "Admin"
    INTERN = "Intern"

class User(BaseModel):
    id: str
    name: str
    username: str
    role: UserRole
    security_id: Optional[str]
    created_at: datetime
    modified_at: datetime

class Users(BaseModel):
    users: list[User]