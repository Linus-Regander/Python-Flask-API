from internal.model.exception.custom import BadRequestException, NotFoundException
from internal.model.user.user import User, Users, UserParams

ERR_INVALID_USER_ID = "Invalid user id"
ERR_USER_NOT_FOUND = "User not found"

class UserRepository:
    def __init__(self, logger, db):
        self.db = db
        self.logger = logger

    ## TODO: Implement repository db methods.

    def get_user_by_id(self, user_id: str) -> User:
        pass

    def get_users(self) -> Users:
        pass

    def create_user(self, user: User):
        pass

    def update_user(self, user_id, user: User):
        pass

    def delete_user(self, user_id: str):
        pass
