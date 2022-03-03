from flask import Flask

from logging_service.logging import logging


def init_app():

    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(logging)

    @app.route("/")
    @app.route("/_health")
    def index():
        return {
            "status": "OK"
        }

    return app
