from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options[config_name])
    
    from .api.v1.__init__ import version1
    app.register_blueprint(version1)


# Creating the app configurations
    db.init_app(app)
    

    return app

    




    
    