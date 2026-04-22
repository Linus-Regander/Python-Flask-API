from flask_restx import Api
from custom import AppException

class ErrorHandler:
    def __init__(self, api: Api):
        self.api = api

    def set_error_handler(self):
        @self.api.errorhandler(AppException)
        def error_handler(e: AppException):
            return {
                "error": e.error_message,
                "message": e.message,
                "status": e.status_code
            }, e.status_code