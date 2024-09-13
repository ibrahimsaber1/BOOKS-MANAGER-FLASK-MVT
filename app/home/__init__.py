from flask import Blueprint

# Declare the blueprint, but don't import views yet
home_routes = Blueprint('home', __name__, url_prefix='', static_folder='static', template_folder='templates')

# Import views at the bottom to avoid circular imports
from app.home import home  # Import after blueprint is declared
