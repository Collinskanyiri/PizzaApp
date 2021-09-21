from flask_restful import Api
from flask import Blueprint

version1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(version1, catch_all_404s=True)

from app.api.v1.views.views import User

api.add_resource(User, '/api/user')

