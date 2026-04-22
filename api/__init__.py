from flask_restx import Api
from api.users import user_namespace

api = Api(
    prefix='/api',
    version='1.0',
    title='User API',
    description='API for handling of user data'
)

api.add_namespace(user_namespace)