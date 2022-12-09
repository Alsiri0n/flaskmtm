from flask import Flask
from .config import TestingConfig, DevelopmentConfig, ProductionConfig

profilies = {
    "development": DevelopmentConfig(),
    "production": ProductionConfig(),
    "testing": TestingConfig(),
}


def create_app(profile: str):
    """
    Create app with use factory pattern and loading config
    """
    app = Flask(__name__)
    app.config.from_object(profilies[profile])

    from flaskmtm.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
