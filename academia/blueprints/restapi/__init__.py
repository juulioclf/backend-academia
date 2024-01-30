from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from .resources import UserItemResource, UserResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)
CORS(bp)


def init_app(app):
    api.add_resource(UserResource, "/users/")
    api.add_resource(UserItemResource, "/user/<id>")
    app.register_blueprint(bp)
