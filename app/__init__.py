import os
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    )
    CORS(app)

    from flask_sslify import SSLify
    if 'DYNO' in os.environ:  # only trigger SSLify if app on Heroku
        sslify = SSLify(app)

    from app.controller import api
    app.register_blueprint(api.bp)

    return app
