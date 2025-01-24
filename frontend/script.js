document.getElementById('load-ingredients').addEventListener('click', loadIngredients);

async function loadIngredients() {
    try {
        // Fetch ingredients from the Flask API
        const response = await fetch('http://127.0.0.1:5000/ingredients');
        
        // Check if the request was successful
        if (response.ok) {
            const ingredients = await response.json();

            // Clear the ingredients list before adding new data
            const ingredientsList = document.getElementById('ingredients-list');
            ingredientsList.innerHTML = '';

            // Loop through ingredients and display them
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
        } else {
            alert('Failed to load ingredients');
        }
    } catch (error) {
        console.error('Error fetching ingredients:', error);
        alert('An error occurred while fetching ingredients');
    }
}
