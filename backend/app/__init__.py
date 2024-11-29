from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .routes import main_bp
import logging


def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    # Load environment variables
    load_dotenv()

    # Initialize Flask app
    app = Flask(__name__)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Load app configuration from a config object
    try:
        app.config.from_object('config.Config')
    except ImportError as e:
        logging.error(f"Error importing configuration: {e}")
        raise RuntimeError("Configuration import failed. Ensure 'config.Config' exists.")

    # Register the main blueprint for routes
    try:
        app.register_blueprint(main_bp)
        logging.info("Blueprint registered successfully.")
    except Exception as e:
        logging.error(f"Error registering blueprint: {e}")
        raise RuntimeError("Blueprint registration failed.")

    # Return the configured app
    return app
