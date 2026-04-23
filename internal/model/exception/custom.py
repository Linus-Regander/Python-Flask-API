class AppException(Exception):
    default_message = "Internal"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)
        self.message = message or self.default_message

class BadRequestException(AppException):
    default_message = "Bad request"

class NotFoundException(AppException):
    default_message = "Not found"

class ConflictException(AppException):
    default_message = "Conflict"

class UnauthenticatedException(AppException):
    default_message = "Unauthenticated"

class UnauthorizedException(AppException):
    default_message = "Forbidden"