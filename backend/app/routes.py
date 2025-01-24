from flask import Blueprint, jsonify, request
from app.models import Ingredient
from app import db

main = Blueprint("main", __name__)

# GET all ingredients
@main.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = Ingredient.query.all()
    ingredient_list = [
        {
            "id": ingredient.id,
            "recipe_name": ingredient.recipe_name,
            "ingredient_name": ingredient.ingredient_name,
            "aisle_number": ingredient.aisle_number,
            "substitute": ingredient.substitute,
        }
        for ingredient in ingredients
    ]
    return jsonify(ingredient_list), 200

# POST: Add a new ingredient
@main.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.get_json()

    recipe_name = data.get("recipe_name")
    ingredient_name = data.get("ingredient_name")
    aisle_number = data.get("aisle_number")
    substitute = data.get("substitute")

    if not recipe_name or not ingredient_name or not aisle_number:
        return jsonify({"error": "Missing required fields"}), 400

    new_ingredient = Ingredient(
        recipe_name=recipe_name,
        ingredient_name=ingredient_name,
        aisle_number=aisle_number,
        substitute=substitute,
    )
    db.session.add(new_ingredient)
    db.session.commit()

    return jsonify({
        "message": "Ingredient added successfully",
        "ingredient": {
            "id": new_ingredient.id,
            "recipe_name": new_ingredient.recipe_name,
            "ingredient_name": new_ingredient.ingredient_name,
            "aisle_number": new_ingredient.aisle_number,
            "substitute": new_ingredient.substitute,
        }
    }), 201

# DELETE: Remove an ingredient by ID
@main.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if not ingredient:
        return jsonify({"error": "Ingredient not found"}), 404

    db.session.delete(ingredient)
    db.session.commit()

    return jsonify({"message": "Ingredient deleted successfully"}), 200

# PUT: Update an ingredient by ID
@main.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if not ingredient:
        return jsonify({"error": "Ingredient not found"}), 404

    data = request.get_json()

    ingredient.recipe_name = data.get("recipe_name", ingredient.recipe_name)
    ingredient.ingredient_name = data.get("ingredient_name", ingredient.ingredient_name)
    ingredient.aisle_number = data.get("aisle_number", ingredient.aisle_number)
    ingredient.substitute = data.get("substitute", ingredient.substitute)

    db.session.commit()

    return jsonify({
        "message": "Ingredient updated successfully",
        "ingredient": {
            "id": ingredient.id,
            "recipe_name": ingredient.recipe_name,
            "ingredient_name": ingredient.ingredient_name,
            "aisle_number": ingredient.aisle_number,
            "substitute": ingredient.substitute,
        }
    }), 200
