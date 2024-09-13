from flask import Flask
from app.config import DevelopmentConfig  # Import your configuration
from app.models import db  # SQLAlchemy instance
from app.books import books_routes 
from app.home import home_routes
from app.auth import auth_routes
import os
import base64

def b64encode_filter(data):
    """Custom filter to encode binary data to base64."""
    return base64.b64encode(data).decode('utf-8')

def create_app(config_type='dev'):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key_for_dev')
    # Initialize extensions
    db.init_app(app)

    # Register blueprints after app is created
    with app.app_context():

        app.register_blueprint(home_routes)
        app.register_blueprint(auth_routes)
        app.register_blueprint(books_routes) 
        
    # Register the custom filter
    app.jinja_env.filters['b64encode'] = b64encode_filter

    return app
