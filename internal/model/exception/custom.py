class AppException(Exception):
    status_code = 500
    error_message = "Internal"

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class BadRequestException(AppException):
    status_code = 400
    error_message = "Bad request"

class NotFoundException(AppException):
    status_code = 404
    error_message = "Not found"

class ConflictException(AppException):
    status_code = 409
    error_message = "Conflict"

class UnauthenticatedException(AppException):
    status_code = 401
    error_message = "Unauthenticated"

class UnauthorizedException(AppException):
    status_code = 403
    error_message = "Forbidden"