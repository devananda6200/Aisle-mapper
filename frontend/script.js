document.getElementById('load-ingredients').addEventListener('click', loadIngredients);
document.getElementById('search-recipe').addEventListener('click', searchRecipe);

async function loadIngredients() {
    try {
        const response = await fetch('http://127.0.0.1:5000/ingredients');
        
        if (response.ok) {
            const ingredients = await response.json();
            displayIngredients(ingredients);
        } else {
            alert('Failed to load ingredients');
        }
    } catch (error) {
        console.error('Error fetching ingredients:', error);
        alert('An error occurred while fetching ingredients');
    }
}

async function searchRecipe() {
    const recipeName = document.getElementById('recipe-name').value;
    
    if (!recipeName) {
        alert('Please enter a recipe name');
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/ingredients/search?recipe_name=${recipeName}`);
        
        if (response.ok) {
            const ingredients = await response.json();
            displayIngredients(ingredients);
        } else {
            alert('No ingredients found for this recipe');
        }
    } catch (error) {
        console.error('Error searching for recipe:', error);
        alert('An error occurred while searching for the recipe');
    }
}

function displayIngredients(ingredients) {
    const ingredientsList = document.getElementById('ingredients-list');
    ingredientsList.innerHTML = '';

    ingredients.forEach(ingredient => {
        const ingredientCard = document.createElement('div');
        ingredientCard.classList.add('ingredient-card');
        ingredientCard.innerHTML = `
            <h3>${ingredient.recipe_name}</h3>
            <p><strong>Ingredient:</strong> ${ingredient.ingredient_name}</p>
            <p><strong>Aisle:</strong> ${ingredient.aisle_number}</p>
            <p><strong>Substitute:</strong> ${ingredient.substitute || 'N/A'}</p>
        `;
        ingredientsList.appendChild(ingredientCard);
    });
}
