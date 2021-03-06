from flask import config


class Config:
    """This defines the factors that are same for the whole application
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collins:12345@localhost/pizzaapp'

class DevConfig(Config):
    """This defines the configurations in development

    Args:
        Config ([type]): [description]
    """


config_options = {
    'development':DevConfig
    }