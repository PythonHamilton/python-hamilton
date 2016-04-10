from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from .views.main import main


environments = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
}


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    if config is not None:
        app.config.from_object(environments.get(config))
    else:  # default to development config
        app.config.from_object("config.DevelopmentConfig")
    app.config.from_pyfile("config.py")  # instance-based config

    app.register_blueprint(main)

    return app
