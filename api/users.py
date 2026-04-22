from flask_restx import Namespace, Resource, fields

from internal.model.user.user import User
from internal.repository.user_repository import UserRepository

user_namespace = Namespace('users', description='user for handling users')

user_model = user_namespace.model("User", {
    "id": fields.String(readonly=True),
    "name": fields.String(required=True),
    "username": fields.String(required=True),
    "role": fields.String(required=True),
})

@user_namespace.route('')
class UsersResource(Resource):
    def __init__(self, logger=None, db=None, api=None, *args, **kwargs):
        self.repository = UserRepository(logger=logger, db=db)
        super().__init__(api=api, args=args, kwargs=kwargs)

    @user_namespace.expect(user_model, validate=True)
    @user_namespace.marshal_with(user_model)
    @user_namespace.response(201, 'user created')
    def post(self) -> User:
        payload = self.api.payload
        return self.repository.create_user(payload)

    @user_namespace.expect(user_model, validate=True)
    @user_namespace.marshal_list_with(user_model)
    def get(self):
        return self.repository.get_users()

@user_namespace.route('/<string:user_id>')
@user_namespace.param('user_id', 'ID of user')
@user_namespace.response(404, 'user not found')
class UserResource(Resource):
    def __init__(self, logger=None, db=None, api=None, *args, **kwargs):
        self.repository = UserRepository(logger=logger, db=db)
        super().__init__(api=api, args=args, kwargs=kwargs)

    @user_namespace.marshal_with(user_model)
    def get(self, user_id: str) -> User:
        return self.repository.get_user_by_id(user_id)

    @user_namespace.expect(user_model, validate=True)
    @user_namespace.marshal_with(user_model)
    @user_namespace.response(204, 'user updated')
    def put(self, user_id: str):
        payload = self.api.payload
        return self.repository.update_user(user_id, payload)

    @user_namespace.response(204, 'user deleted')
    def delete(self, user_id: str):
        self.repository.delete_user(user_id)
        return 'user deleted', 204