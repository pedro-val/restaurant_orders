# Req 3
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self.all_dishes()

    def read_file(self):
        with open(self.source_path, 'r') as file:
            lines = file.readlines()

        data = {}
        for index, line in enumerate(lines):
            if index == 0:
                continue
            parts = line.strip().split(',')

            recipe = parts[0]
            price = float(parts[1])
            ingredient = parts[2]
            recipe_amount = int(parts[3])

            if recipe in data:

                data[recipe]['price'].append(price)
                data[recipe]['ingredient'].append(ingredient)
                data[recipe]['recipe_amount'].append(recipe_amount)
            else:

                data[recipe] = {
                    'price': [price],
                    'ingredient': [ingredient],
                    'recipe_amount': [recipe_amount]
                }
        retorno = {}
        for dish, details in data.items():
            retorno[dish] = {
                'price': details['price'][0],
                'ingredient': list(zip(details['ingredient'],
                                       details['recipe_amount']))
            }
        return retorno

    def all_dishes(self):
        retorno = self.read_file()
        dishes = set()
        for dish in retorno:
            dishes.add(Dish(dish, retorno[dish]['price']))
        for dish in dishes:
            dish = self.add_ingredients(dish, retorno[dish.name]['ingredient'])
        return dishes

    def add_ingredients(self, dish: Dish, ingredients):
        for dish_name in ingredients:
            for ingredient in ingredients:
                dish.add_ingredient_dependency(
                    Ingredient(ingredient[0]), ingredient[1])
