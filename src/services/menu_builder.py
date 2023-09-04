from typing import Dict, List
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"

DATA_PATH = "tests/mocks/menu_base_data.csv"
INVENTORY_PATH = "tests/mocks/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes = self.menu_data.dishes
        for dish in dishes:
            if self.inventory.check_recipe_availability(dish.recipe) is False:
                return []
        return self.mount_menu(dishes, restriction)

    def mount_menu(self, dishes, restriction=None) -> List[Dict]:
        retorno = []
        for dish in dishes:
            retorno.append(
                {
                    "dish_name": dish.name,
                    "ingredients": dish.get_ingredients(),
                    "price": dish.price,
                    "restrictions": dish.get_restrictions(),
                }
            )
        if restriction:
            return self.filter_restrictions(retorno, restriction)
        else:
            return sorted(retorno, key=lambda dish: dish['dish_name'])

    def filter_restrictions(self, dishes, restriction):
        retorno = []
        for dish in dishes:
            if restriction not in dish['restrictions']:
                retorno.append(dish)
        return sorted(retorno, key=lambda dish: dish['dish_name'])

    def checking_inventory(self, dish):
        try:
            self.inventory.consume_recipe(dish.recipe)
            return True
        except ValueError:
            return False
