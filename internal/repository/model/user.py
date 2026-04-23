from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Enum

from internal.model.user.user import UserRole, User

Base = declarative_base()

class UserBase(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    username = Column(String)
    role = Column(Enum(UserRole))
    security_id = Column(String, nullable=True)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)

def to_schema(user: UserBase) -> User:
    return User(
        id=user.id,
        name=user.name,
        username=user.username,
        role=user.role,
        security_id=user.security_id,
        created_at=user.created_at,
        modified_at=user.modified_at,
    )