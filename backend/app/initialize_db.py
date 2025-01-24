import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Ingredient

# Initialize the app and the database
app = create_app()

with app.app_context():
    db.create_all()
    print("Database initialized and tables created.")
