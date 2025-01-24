import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Ingredient

app = create_app()

with app.app_context():
    try:
        # Check if ingredients already exist to prevent duplicates
        existing_ingredients = Ingredient.query.all()
        if existing_ingredients:
            print("Data already exists, skipping seed.")
        else:
            ingredients = [
                Ingredient(recipe_name="Pancakes", ingredient_name="Flour", aisle_number="Aisle 2", substitute="Almond Flour"),
                Ingredient(recipe_name="Pancakes", ingredient_name="Eggs", aisle_number="Aisle 5", substitute="Flaxseed Meal"),
                Ingredient(recipe_name="Salad", ingredient_name="Lettuce", aisle_number="Aisle 1", substitute="Spinach"),
            ]

            # Bulk insert the ingredients
            db.session.bulk_save_objects(ingredients)
            db.session.commit()
            print("Sample data added!")
    
    except Exception as e:
        print(f"An error occurred while adding seed data: {e}")
