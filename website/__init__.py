import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    # Creating an object that will represent the app
    app = Flask(__name__)

    #Creating a secret key for the cookies
    app.config['SECRET_KEY'] = 'kwo31201iasep12kj123123'

    #Importing the blueprints from these python modules
    from .views import views
    from .auth import auth

    #Registering the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
