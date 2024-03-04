spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicy_food['name'] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level']>5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        emoji_for_heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_for_heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food['cuisine']==cuisine:
            return spicy_food
    return None

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        emoji_for_heat_level = "🌶" * spicy_food["heat_level"]
        if spicy_food['heat_level']>5:
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {emoji_for_heat_level}")
    
def get_average_heat_level(spicy_foods):
    total_heat_level=sum(spicy_food['heat_level'] for spicy_food in spicy_foods)
    number_of_spicy_foods=len(spicy_foods)
    return total_heat_level//number_of_spicy_foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
