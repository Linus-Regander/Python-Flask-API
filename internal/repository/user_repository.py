from typing import cast

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from internal.model.exception.custom import BadRequestException, NotFoundException, AppException
from internal.model.user.user import User, Users
from internal.repository.model.user import UserBase, to_schema

#
# Errors.
#

ERR_INVALID_USER_ID = "Invalid user id"
ERR_USER_NOT_FOUND = "User not found"
ERR_USERS_NOT_FOUND = "Users not found"
ERR_MISSING_PAYLOAD = "Payload is missing"

class UserRepository:
    def __init__(self, logger, db: Session):
        self.db = db
        self.logger = logger

    def get_user_by_id(self, user_id: str) -> User:
        if not user_id:
            raise BadRequestException(ERR_INVALID_USER_ID)

        result = self.db.execute(
            select(UserBase).where(User.id == user_id)
        )

        user = result.scalar_one_or_none()
        if user is None:
            raise NotFoundException(ERR_USER_NOT_FOUND)

        return to_schema(cast(UserBase, user))

    def get_users(self, limit: int = 10, offset: int = 0) -> Users:
        result = self.db.execute(
            select(UserBase).offset(offset).limit(limit)
        )

        users = list(result.scalars().all())
        if not users:
            raise NotFoundException(ERR_USERS_NOT_FOUND)

        return Users(users=users)

    def create_user(self, payload: User):
        if not payload:
            raise BadRequestException(ERR_MISSING_PAYLOAD)

        try:
            self.db.add(payload)
            self.db.commit()
            self.db.refresh(payload)
            return payload

        except Exception as e:
            self.db.rollback()
            raise AppException(str(e))

    def update_user(self, user_id: str, payload: User):
        if not user_id:
            raise BadRequestException(ERR_INVALID_USER_ID)

        if not payload:
            raise BadRequestException(ERR_MISSING_PAYLOAD)

        update_data = {
            k: v for k, v in payload.model_dump().items()
            if v is not None
        }

        if not update_data:
            raise BadRequestException(ERR_MISSING_PAYLOAD)

        try:
            result = self.db.execute(update(UserBase).where(User.id == user_id).values(**update_data))
            if result.scalar_one_or_none() is None:
                raise NotFoundException(ERR_USER_NOT_FOUND)

            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise AppException(str(e))

    def delete_user(self, user_id: str):
        if not user_id:
            raise BadRequestException(ERR_INVALID_USER_ID)

        try:
            result = self.db.execute(delete(UserBase).where(User.id == user_id))
            if result.scalar_one_or_none() is None:
                raise NotFoundException(ERR_USER_NOT_FOUND)

            self.db.commit()

        except Exception as e:
            self.db.rollback()
            raise AppException(str(e))
