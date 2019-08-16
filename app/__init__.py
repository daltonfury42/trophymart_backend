from flask import Flask

from app.config import configs


def create_app(environment='development'):
    app = Flask(__name__)
    app.config.from_object(configs[environment])

    from .resources import pricing
    app.register_blueprint(pricing.pricing)

    return app
