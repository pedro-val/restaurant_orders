from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction

ANIMAL_MEAT = 'ANIMAL_MEAT'
ANIMAL_DERIVED = 'ANIMAL_DERIVED'


def test_ingredient():
    ingrediente = Ingredient("bacon")
    assert ingrediente.__hash__() == hash('bacon')
    assert ingrediente.__eq__(ingrediente) is True
    assert ingrediente.__eq__("bacon") is False
    assert ingrediente.__repr__() == "Ingredient('bacon')"
    assert ingrediente.name == "bacon"
    assert ingrediente.restrictions == {Restriction.ANIMAL_MEAT,
                                        Restriction.ANIMAL_DERIVED}
