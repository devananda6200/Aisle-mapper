import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    # Explicitly declare the SQL as a text object
    db.session.execute(text("DROP TABLE IF EXISTS ingredients"))
    db.session.commit()
    print("Dropped 'ingredients' table.")
