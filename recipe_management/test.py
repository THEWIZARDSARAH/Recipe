import requests

# Base URL of the API
BASE_URL = 'http://localhost:8000/api/'

# Endpoints
USERS_URL = f'{BASE_URL}users/'
RECIPES_URL = f'{BASE_URL}recipes/'
TOKEN_URL = f'{BASE_URL}token/'
TOKEN_REFRESH_URL = f'{BASE_URL}token/refresh/'

# User credentials
USER_DATA = {
    'username': 'rrrrrrrr',
    'email': 'rocky11@gmail.com',
    'password': 'slovakiaslovakiannslovakianslovakian',
     'is_staff':'yes',
        'is_superuser':'yes'
}

UPDATED_USER_DATA = {
    'username': 'john_doe_updated',
    'email': 'john_updated@example.com',
    'password': 'newsecurepassword456'
}

# Recipe data
RECIPE_DATA = {
    "title": "Chocolate Cake",
    "description": "Delicious and rich chocolate cake.",
    "ingredients": ["flour", "sugar", "cocoa powder", "eggs", "butter"],
    "instructions": "Mix ingredients and bake for 30 minutes.",
    "category": "Dessert",
    "preparation_time": 20,
    "cooking_time": 30,
    "servings": 8
}

UPDATED_RECIPE_DATA = {
    "title": "Vanilla Cake",
    "description": "Light and fluffy vanilla cake.",
    "ingredients": ["flour", "sugar", "vanilla extract", "eggs", "butter"],
    "instructions": "Mix ingredients and bake for 25 minutes.",
    "category": "Dessert",
    "preparation_time": 15,
    "cooking_time": 25,
    "servings": 6
}


def create_user(user_data):
    response = requests.post(USERS_URL, data=user_data)
    if response.status_code == 201:
        print("User created successfully.")

        return response.json()
    else:
        print(f"Failed to create user: {response.status_code}")
        print(response.json())
        return None


def list_users():
    response = requests.get(USERS_URL)
    if response.status_code == 200:
        print("List of Users:")
        for user in response.json():
            print(user)
    else:
        print(f"Failed to list users: {response.status_code}")
        print(response.json())


def retrieve_user(user_id):
    response = requests.get(f'{USERS_URL}{user_id}/')
    if response.status_code == 200:
        print("User Details:")
        print(response.json())
    else:
        print(f"Failed to retrieve user: {response.status_code}")
        print(response.json())


def update_user(user_id, updated_data, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.put(f'{USERS_URL}{user_id}/', data=updated_data, headers=headers)
    if response.status_code in [200, 202]:
        print("User updated successfully.")
        return response.json()
    else:
        print(f"Failed to update user: {response.status_code}")
        print(response.json())
        return None


def delete_user(user_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f'{USERS_URL}{user_id}/', headers=headers)
    if response.status_code == 204:
        print("User deleted successfully.")
    else:
        print(f"Failed to delete user: {response.status_code}")
        print(response.json())


def obtain_token(username, password):
    response = requests.post(TOKEN_URL, data={'username': username, 'password': password})
    if response.status_code == 200:
        tokens = response.json()
        print("Obtained JWT tokens.")
        print(tokens)
        return tokens
    else:
        print(f"Failed to obtain token: {response.status_code}")
        print(response.json())
        return None


def refresh_token(refresh_token):
    response = requests.post(TOKEN_REFRESH_URL, data={'refresh': refresh_token})
    if response.status_code == 200:
        new_tokens = response.json()
        print("Refreshed JWT tokens.")
        print(new_tokens)
        return new_tokens
    else:
        print(f"Failed to refresh token: {response.status_code}")
        print(response.json())
        return None


def create_recipe(recipe_data, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(RECIPES_URL, json=recipe_data, headers=headers)
    if response.status_code == 201:
        print("Recipe created successfully.")
        return response.json()
    else:
        print(f"Failed to create recipe: {response.status_code}")
        print(response.json())
        return None


def list_recipes():
    response = requests.get(RECIPES_URL)
    if response.status_code == 200:
        print("List of Recipes:")
        for recipe in response.json()['results']:  # Assuming pagination
            print(recipe)
    else:
        print(f"Failed to list recipes: {response.status_code}")
        print(response.json())


def retrieve_recipe(recipe_id):
    response = requests.get(f'{RECIPES_URL}{recipe_id}/')
    if response.status_code == 200:
        print("Recipe Details:")
        print(response.json())
    else:
        print(f"Failed to retrieve recipe: {response.status_code}")
        print(response.json())


def update_recipe(recipe_id, updated_data, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.put(f'{RECIPES_URL}{recipe_id}/', json=updated_data, headers=headers)
    if response.status_code in [200, 202]:
        print("Recipe updated successfully.")
        return response.json()
    else:
        print(f"Failed to update recipe: {response.status_code}")
        print(response.json())
        return None


def delete_recipe(recipe_id, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.delete(f'{RECIPES_URL}{recipe_id}/', headers=headers)
    if response.status_code == 204:
        print("Recipe deleted successfully.")
    else:
        print(f"Failed to delete recipe: {response.status_code}")
        print(response.json())


def search_recipes(query):
    params = {'search': query}
    response = requests.get(RECIPES_URL, params=params)
    if response.status_code == 200:
        print(f"Search Results for '{query}':")
        for recipe in response.json()['results']:
            print(recipe)
    else:
        print(f"Failed to search recipes: {response.status_code}")
        print(response.json())


def main():
    print("=== Recipe Management API Client ===\n")

    # 1. Create a new user
    print("1. Creating a new user...")
    user = create_user(USER_DATA)
    if not user:
        return
    print(user.keys())
    # 2. Obtain JWT tokens
    print("\n2. Obtaining JWT tokens...")
    tokens = obtain_token(USER_DATA['username'], USER_DATA['password'])
    if not tokens:
        return
    access_token = tokens['access']
    refresh_token_str = tokens['refresh']

    # 3. Create a new recipe
    print("\n3. Creating a new recipe...")
    recipe = create_recipe(RECIPE_DATA, access_token)
    if not recipe:
        return
    recipe_id = recipe['id']

    # 4. List all recipes
    print("\n4. Listing all recipes...")
    list_recipes()

    # 5. Retrieve the specific recipe
    print("\n5. Retrieving the created recipe...")
    retrieve_recipe(recipe_id)

    # 6. Update the recipe
    print("\n6. Updating the recipe...")
    updated_recipe = update_recipe(recipe_id, UPDATED_RECIPE_DATA, access_token)
    if updated_recipe:
        retrieve_recipe(recipe_id)

    # 7. Search for recipes containing 'Vanilla'
    print("\n7. Searching for recipes containing 'Vanilla'...")
    search_recipes('Vanilla')

    # 8. Refresh the JWT token
    print("\n8. Refreshing the JWT token...")
    new_tokens = refresh_token(refresh_token_str)
    if new_tokens:
        access_token = new_tokens['access']

    # 9. Update user details
    print("\n9. Updating user details...")
    user_id = user['id']
    updated_user = update_user(user_id, UPDATED_USER_DATA, access_token)
    if updated_user:
        retrieve_user(user_id)

    # 10. Delete the recipe
    print("\n10. Deleting the recipe...")
    delete_recipe(recipe_id, access_token)

    # 11. Delete the user
    print("\n11. Deleting the user...")
    delete_user(user_id, access_token)

    print("\n=== Operations Completed ===")


if __name__ == '__main__':
    main()
