from flask import Flask
from .config import Config
from .db import db

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Load the configuration from the Config class
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Import routes and models here (optional)
    from .routes import main
    app.register_blueprint(main)

    return app
