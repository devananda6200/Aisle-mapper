import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Ingredient

app = create_app()

with app.app_context():
    # Insert multiple ingredients for various recipes
    ingredients = [
        # Dal Tadka Recipe
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Yellow Lentils (Toor Dal)", aisle_number="Aisle 1", substitute="Moong dal or masoor dal"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Onion", aisle_number="Aisle 2", substitute="Shallots or leeks"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Garlic", aisle_number="Aisle 3", substitute="Garlic paste or garlic powder"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Ginger", aisle_number="Aisle 4", substitute="Ginger paste or fresh ginger"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Tomato", aisle_number="Aisle 5", substitute="Canned tomatoes or tomato puree"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Turmeric Powder", aisle_number="Aisle 6", substitute="No replacement needed"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Cumin Seeds", aisle_number="Aisle 7", substitute="Fennel seeds or caraway seeds"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Mustard Seeds", aisle_number="Aisle 8", substitute="Sesame seeds or carom seeds"),
        Ingredient(recipe_name="Dal Tadka", ingredient_name="Ghee", aisle_number="Aisle 9", substitute="Butter or vegetable oil"),

        # Palak Paneer Recipe
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Spinach", aisle_number="Aisle 1", substitute="Kale or Swiss chard"),
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Paneer", aisle_number="Aisle 2", substitute="Tofu or cottage cheese"),
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Onion", aisle_number="Aisle 3", substitute="Shallots or spring onions"),
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Garlic", aisle_number="Aisle 4", substitute="Garlic powder or garlic paste"),
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Tomato", aisle_number="Aisle 5", substitute="Tomato puree or canned tomatoes"),
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Garam Masala", aisle_number="Aisle 6", substitute="Homemade spice mix (cumin, coriander)"),
        Ingredient(recipe_name="Palak Paneer", ingredient_name="Cream", aisle_number="Aisle 7", substitute="Coconut cream or cashew cream"),

        # Chole Bhature Recipe
        Ingredient(recipe_name="Chole Bhature", ingredient_name="Chickpeas", aisle_number="Aisle 1", substitute="Black-eyed peas or kidney beans"),
        Ingredient(recipe_name="Chole Bhature", ingredient_name="Onion", aisle_number="Aisle 2", substitute="Shallots or leeks"),
        Ingredient(recipe_name="Chole Bhature", ingredient_name="Tomatoes", aisle_number="Aisle 3", substitute="Tomato paste or canned tomatoes"),
        Ingredient(recipe_name="Chole Bhature", ingredient_name="Garam Masala", aisle_number="Aisle 4", substitute="Homemade spice mix (cumin, coriander)"),
        Ingredient(recipe_name="Chole Bhature", ingredient_name="Bhature Flour", aisle_number="Aisle 5", substitute="Whole wheat flour or gluten-free flour"),
        Ingredient(recipe_name="Chole Bhature", ingredient_name="Baking Soda", aisle_number="Aisle 6", substitute="Baking powder or yeast"),

        # Samosa Recipe
        Ingredient(recipe_name="Samosa", ingredient_name="Potatoes", aisle_number="Aisle 1", substitute="Sweet potatoes or pumpkin"),
        Ingredient(recipe_name="Samosa", ingredient_name="Green Peas", aisle_number="Aisle 2", substitute="Corn kernels or carrots"),
        Ingredient(recipe_name="Samosa", ingredient_name="Onion", aisle_number="Aisle 3", substitute="Shallots or green onions"),
        Ingredient(recipe_name="Samosa", ingredient_name="Cumin Seeds", aisle_number="Aisle 4", substitute="Caraway seeds or fennel seeds"),
        Ingredient(recipe_name="Samosa", ingredient_name="Green Chilies", aisle_number="Aisle 5", substitute="Red chili flakes or black pepper"),
        Ingredient(recipe_name="Samosa", ingredient_name="Hing (Asafoetida)", aisle_number="Aisle 6", substitute="Onion powder (optional)"),

        # Dosa Recipe
        Ingredient(recipe_name="Dosa", ingredient_name="Rice Flour", aisle_number="Aisle 1", substitute="Buckwheat flour or quinoa flour"),
        Ingredient(recipe_name="Dosa", ingredient_name="Urad Dal (Black Gram)", aisle_number="Aisle 2", substitute="Moong dal or chickpea flour"),
        Ingredient(recipe_name="Dosa", ingredient_name="Fenugreek Seeds", aisle_number="Aisle 3", substitute="Fennel seeds or cumin seeds"),
        Ingredient(recipe_name="Dosa", ingredient_name="Ghee", aisle_number="Aisle 4", substitute="Butter or vegetable oil"),

        # Rogan Josh Recipe
        Ingredient(recipe_name="Rogan Josh", ingredient_name="Lamb", aisle_number="Aisle 1", substitute="Chicken or tofu (for a vegetarian version)"),
        Ingredient(recipe_name="Rogan Josh", ingredient_name="Yogurt", aisle_number="Aisle 2", substitute="Cashew cream or coconut milk"),
        Ingredient(recipe_name="Rogan Josh", ingredient_name="Garam Masala", aisle_number="Aisle 3", substitute="Homemade spice mix (cumin, coriander, cardamom)"),
        Ingredient(recipe_name="Rogan Josh", ingredient_name="Onion", aisle_number="Aisle 4", substitute="Shallots or leeks"),

        # Aloo Gobi Recipe
        Ingredient(recipe_name="Aloo Gobi", ingredient_name="Potatoes", aisle_number="Aisle 1", substitute="Sweet potatoes or turnips"),
        Ingredient(recipe_name="Aloo Gobi", ingredient_name="Cauliflower", aisle_number="Aisle 2", substitute="Broccoli or Brussels sprouts"),
        Ingredient(recipe_name="Aloo Gobi", ingredient_name="Cumin Seeds", aisle_number="Aisle 3", substitute="Caraway seeds or fennel seeds"),
        Ingredient(recipe_name="Aloo Gobi", ingredient_name="Turmeric Powder", aisle_number="Aisle 4", substitute="No replacement needed"),
        Ingredient(recipe_name="Aloo Gobi", ingredient_name="Coriander Powder", aisle_number="Aisle 5", substitute="Cilantro leaves or parsley"),
        Ingredient(recipe_name="Aloo Gobi", ingredient_name="Green Chilies", aisle_number="Aisle 6", substitute="Red chili flakes or black pepper"),

        # Kadhi Pakora Recipe
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Gram Flour (Besan)", aisle_number="Aisle 1", substitute="Chickpea flour or rice flour"),
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Yogurt", aisle_number="Aisle 2", substitute="Cashew yogurt or coconut milk"),
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Onion", aisle_number="Aisle 3", substitute="Shallots or leeks"),
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Ginger", aisle_number="Aisle 4", substitute="Ginger powder or ginger paste"),
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Turmeric Powder", aisle_number="Aisle 5", substitute="No replacement needed"),
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Mustard Seeds", aisle_number="Aisle 6", substitute="Sesame seeds or cumin seeds"),
        Ingredient(recipe_name="Kadhi Pakora", ingredient_name="Curry Leaves", aisle_number="Aisle 7", substitute="Coriander leaves or bay leaves"),

        # Tandoori Chicken Recipe
        Ingredient(recipe_name="Tandoori Chicken", ingredient_name="Chicken", aisle_number="Aisle 1", substitute="Tofu or paneer (for a vegetarian version)"),
        Ingredient(recipe_name="Tandoori Chicken", ingredient_name="Yogurt", aisle_number="Aisle 2", substitute="Cashew cream or coconut yogurt"),
        Ingredient(recipe_name="Tandoori Chicken", ingredient_name="Ginger-Garlic Paste", aisle_number="Aisle 3", substitute="Fresh ginger and garlic, minced"),
        Ingredient(recipe_name="Tandoori Chicken", ingredient_name="Lemon Juice", aisle_number="Aisle 4", substitute="Vinegar or lime juice"),
        Ingredient(recipe_name="Tandoori Chicken", ingredient_name="Garam Masala", aisle_number="Aisle 5", substitute="Homemade spice mix (cumin, coriander, cardamom)"),

        # Pav Bhaji Recipe
        Ingredient(recipe_name="Pav Bhaji", ingredient_name="Mixed Vegetables (Potatoes, Cauliflower, Peas, Carrots)", aisle_number="Aisle 1", substitute="Any vegetables like sweet potatoes, corn, or zucchini"),
        Ingredient(recipe_name="Pav Bhaji", ingredient_name="Pav (Bread Rolls)", aisle_number="Aisle 2", substitute="Gluten-free buns or whole wheat rolls"),
        Ingredient(recipe_name="Pav Bhaji", ingredient_name="Butter", aisle_number="Aisle 3", substitute="Margarine or ghee"),
        Ingredient(recipe_name="Pav Bhaji", ingredient_name="Pav Bhaji Masala", aisle_number="Aisle 4", substitute="Homemade masala mix (cumin, coriander, garam masala)"),

        # Matar Paneer Recipe
        Ingredient(recipe_name="Matar Paneer", ingredient_name="Paneer", aisle_number="Aisle 1", substitute="Tofu or cottage cheese"),
        Ingredient(recipe_name="Matar Paneer", ingredient_name="Green Peas", aisle_number="Aisle 2", substitute="Corn or green beans"),
        Ingredient(recipe_name="Matar Paneer", ingredient_name="Tomatoes", aisle_number="Aisle 3", substitute="Canned tomatoes or tomato puree"),
        Ingredient(recipe_name="Matar Paneer", ingredient_name="Ginger", aisle_number="Aisle 4", substitute="Ginger paste or fresh ginger"),
        Ingredient(recipe_name="Matar Paneer", ingredient_name="Garam Masala", aisle_number="Aisle 5", substitute="Homemade spice mix (cumin, coriander)"),

        # Korma Recipe
        Ingredient(recipe_name="Korma", ingredient_name="Meat (Lamb/Chicken)", aisle_number="Aisle 1", substitute="Tofu or soy protein"),
        Ingredient(recipe_name="Korma", ingredient_name="Yogurt", aisle_number="Aisle 2", substitute="Cashew cream or coconut milk"),
        Ingredient(recipe_name="Korma", ingredient_name="Coconut", aisle_number="Aisle 3", substitute="Almonds or cashews"),
        Ingredient(recipe_name="Korma", ingredient_name="Cinnamon", aisle_number="Aisle 4", substitute="Nutmeg or cloves"),

        # Idli Recipe
        Ingredient(recipe_name="Idli", ingredient_name="Rice Flour", aisle_number="Aisle 1", substitute="Buckwheat flour or millet flour"),
        Ingredient(recipe_name="Idli", ingredient_name="Urad Dal (Black Gram)", aisle_number="Aisle 2", substitute="Moong dal or chickpea flour"),
        Ingredient(recipe_name="Idli", ingredient_name="Fenugreek Seeds", aisle_number="Aisle 3", substitute="Fennel seeds or caraway seeds"),
        Ingredient(recipe_name="Idli", ingredient_name="Coconut", aisle_number="Aisle 4", substitute="Coconut milk or cashew cream"),

        # Lassi Recipe
        Ingredient(recipe_name="Lassi", ingredient_name="Yogurt", aisle_number="Aisle 1", substitute="Cashew yogurt or coconut milk"),
        Ingredient(recipe_name="Lassi", ingredient_name="Milk", aisle_number="Aisle 2", substitute="Almond milk or soy milk"),
        Ingredient(recipe_name="Lassi", ingredient_name="Sugar", aisle_number="Aisle 3", substitute="Honey or agave syrup"),

        # Pesarattu Recipe
        Ingredient(recipe_name="Pesarattu", ingredient_name="Green Moong Dal", aisle_number="Aisle 1", substitute="Lentils or chickpeas"),
        Ingredient(recipe_name="Pesarattu", ingredient_name="Rice Flour", aisle_number="Aisle 2", substitute="Millet flour or sorghum flour"),
        Ingredient(recipe_name="Pesarattu", ingredient_name="Ginger", aisle_number="Aisle 3", substitute="Ginger paste or fresh ginger"),
        Ingredient(recipe_name="Pesarattu", ingredient_name="Green Chilies", aisle_number="Aisle 4", substitute="Red chili flakes or black pepper"),

        # Vada Pav Recipe
        Ingredient(recipe_name="Vada Pav", ingredient_name="Potatoes", aisle_number="Aisle 1", substitute="Sweet potatoes or yam"),
        Ingredient(recipe_name="Vada Pav", ingredient_name="Pav (Bread Rolls)", aisle_number="Aisle 2", substitute="Gluten-free bread rolls"),
        Ingredient(recipe_name="Vada Pav", ingredient_name="Green Chilies", aisle_number="Aisle 3", substitute="Jalapenos or chili flakes"),
        Ingredient(recipe_name="Vada Pav", ingredient_name="Hing (Asafoetida)", aisle_number="Aisle 4", substitute="Onion powder (optional)"),

        # Dhokla Recipe
        Ingredient(recipe_name="Dhokla", ingredient_name="Rice Flour", aisle_number="Aisle 1", substitute="Millet flour or chickpea flour"),
        Ingredient(recipe_name="Dhokla", ingredient_name="Chickpea Flour", aisle_number="Aisle 2", substitute="Rice flour or quinoa flour"),
        Ingredient(recipe_name="Dhokla", ingredient_name="Yogurt", aisle_number="Aisle 3", substitute="Cashew yogurt or coconut milk"),
        Ingredient(recipe_name="Dhokla", ingredient_name="Mustard Seeds", aisle_number="Aisle 4", substitute="Cumin seeds or sesame seeds"),


        # Pasta Recipe
        Ingredient(recipe_name="Pasta", ingredient_name="Pasta", aisle_number="Aisle 7", substitute="Zoodles"),
        Ingredient(recipe_name="Pasta", ingredient_name="Tomato Sauce", aisle_number="Aisle 8", substitute="Pesto Sauce"),
        Ingredient(recipe_name="Pasta", ingredient_name="Parmesan", aisle_number="Aisle 9", substitute="Nutritional Yeast"),


        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Raw Jackfruit", aisle_number="Aisle 10", substitute="Raw Breadfruit / Unripe Plantains"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Grated Coconut", aisle_number="Aisle 11", substitute="Coconut Milk / Desiccated Coconut"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Turmeric Powder", aisle_number="Aisle 12", substitute="Saffron / Annatto Powder"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Green Chilies", aisle_number="Aisle 13", substitute="Red Chilies / Chili Powder"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Cumin Seeds", aisle_number="Aisle 14", substitute="Ground Cumin / Fennel Seeds"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Garlic Cloves", aisle_number="Aisle 15", substitute="Shallots / Garlic Powder"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Curry Leaves", aisle_number="Aisle 16", substitute="Coriander Leaves"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Coconut Oil", aisle_number="Aisle 17", substitute="Ghee / Vegetable Oil"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Mustard Seeds", aisle_number="Aisle 18", substitute="Nigella Seeds / Omit"),
        Ingredient(recipe_name="Chakkapuzhukk", ingredient_name="Dried Red Chilies", aisle_number="Aisle 19", substitute="Fresh Red Chilies / Chili Flakes")
    ]

    # Bulk save the ingredients to the database
    db.session.bulk_save_objects(ingredients)
    db.session.commit()
    print("Sample data added!")
