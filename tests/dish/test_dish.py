from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest


ANIMAL_MEAT = 'ANIMAL_MEAT'
ANIMAL_DERIVED = 'ANIMAL_DERIVED'


def test_dish():
    comida = Dish("comida", 10.0)
    assert comida.name == "comida"
    assert comida.price == 10.0
    assert comida.__hash__() == hash("Dish('comida', R$10.00)")
    assert comida.__eq__(comida) is True
    assert comida.__eq__("comida") is False
    assert comida.__repr__() == "Dish('comida', R$10.00)"
    comida.add_ingredient_dependency(Ingredient("bacon"), 1)
    assert comida.get_restrictions() == {Restriction.ANIMAL_MEAT,
                                         Restriction.ANIMAL_DERIVED}
    comida.add_ingredient_dependency(Ingredient("farinha"), 1)
    assert comida.get_ingredients() == {Ingredient("bacon"),
                                        Ingredient("farinha")}
    assert comida.recipe == {Ingredient("bacon"): 1, Ingredient("farinha"): 1}
    with pytest.raises(TypeError) as error:
        Dish("carne", "10")
    assert str(error.value) == "Dish price must be float."
    with pytest.raises(ValueError) as error:
        Dish("carne", -10)
    assert str(error.value) == "Dish price must be greater then zero."
