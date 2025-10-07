import json
import os
from substitutions import get_substitute

# Load recipes.json using absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "recipes.json")

with open(DATA_PATH, "r") as f:
    recipes_data = json.load(f)

def suggest_recipes(available_ingredients):
    """
    Suggest recipes based on available ingredients.
    Uses a greedy approach: allow recipes with up to 2 missing ingredients.
    Returns a list of dictionaries containing:
        - recipe: recipe name
        - missing: list of missing ingredients
        - substitutions: list of lists with possible substitutions
    """
    suggested = []
    available_set = set(available_ingredients)

    for recipe_name, details in recipes_data.items():
        required_set = set(details.get("ingredients", []))
        missing = required_set - available_set

        if len(missing) <= 2:  # Greedy: allow <=2 missing ingredients
            suggested.append({
                "recipe": recipe_name,
                "missing": list(missing),
                "substitutions": [get_substitute(ing) for ing in missing]
            })

    return suggested
