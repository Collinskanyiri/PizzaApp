from app.api.v1.models.models import User,Roles,Pizza,Toppings,Size,Order
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()


parser.add_argument("users-username", type=str, required=True,
                    help="Please input your name")
parser.add_argument("pizza-name", type=str, required=True,
                    help="Please input type pizza")
parser.add_argument("size-name", type=str, required=True,
                    help="Please input  size")
parser.add_argument("toppings-name", type=str, required=True,
                    help="Please input toppings")
parser.add_argument("users-password", type=str, required=True,
                    help="Please input your password")


class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        Register a user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()

        username = args["users-username"]
        password = args["users-password"]
        pizza = args["pizza-name"]
        size = args["size-name"]
        toppings = args["toppings-name"]

        newOrder = Order(username, password, pizza,
                             size, toppings)
        newOrder.save_Order()

        return {
            "message": "User register successfully",
            "user": newOrder.__dict__
        }, 201

    def get(self):
        pass
