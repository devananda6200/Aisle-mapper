from datetime import datetime
from .db import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(255), nullable=False)
    ingredient_name = db.Column(db.String(255), nullable=False)
    aisle_number = db.Column(db.String(50), nullable=False)
    substitute = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Ingredient {self.ingredient_name}>"
