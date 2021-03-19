#to initialize flask and register blueprint
from flask import Flask
from .views import view

#main function wich returns app
def create_app():
    #initialize Flask
    app = Flask(__name__)

    #register the urls
    app.register_blueprint(view, url_prefix='/')

    #return it
    return app
