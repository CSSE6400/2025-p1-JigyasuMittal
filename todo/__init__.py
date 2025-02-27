from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views.routes import api  # Import the Blueprint
    app.register_blueprint(api)  # Register the Blueprint

    return app  # Ensure correct indentation
