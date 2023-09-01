from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction
import pytest

# 2.1 - Será validado que seu teste falha caso o atributo name
# de um prato seja diferente que o passado ao construtor.

# 2.2 - Será validado que seu teste falha caso os hashes
# de dois pratos iguais sejam diferentes;

# 2.3 - Será validado que seu teste falha caso os hashes
# de dois pratos diferentes sejam iguais;

# 2.4 - Será validado que seu teste falha caso a comparação
# de igualdade de dois pratos iguais (ou de um prato com ele mesmo) seja falsa;

# 2.5 - Será validado que seu teste falha caso a comparação
# de igualdade de dois pratos diferentes seja verdadeira;

# 2.6 - Será validado que seu teste falha caso a implementação
# do método __repr__ retorne um valor inadequado;

# 2.7 - Será validado que seu teste falha caso um TypeError
# não seja levantado ao criar um prato com um valor de tipo inválido;

# 2.8 - Será validado que seu teste falha caso um ValueError
# não seja levantado ao criar um prato com um valor inválido;

# 2.9 - Será validado que seu teste falha caso o acesso a um
# valor do atributo recipe, ao ser indexado com um ingrediente válido
#  retorne uma quantidade inválida (dica: use o método get do dicionário,
#  por exemplo dish.recipe.get(ingredient));

# 2.10 - Será validado que seu teste falha caso o método get
# _restrictions retorne um set de restrições diferente do esperado;

# 2.11 - Será validado que seu teste falha caso o método get
# _ingredients retorne um set de ingredientes diferente do esperado;

# 2.12 - Será validado que seu teste passa com a implementação
# correta da classe Dish.

# Req 2

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
