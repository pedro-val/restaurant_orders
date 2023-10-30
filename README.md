# CARDÁPIO DINÂMICO PARA O RESTAURANTE 🍝 🦐 CHAPA QUENTE 🍛 🥘

Este projeto faz parte de um curso intensivo de Full Stack de 1500 horas e tem como objetivo a construção de uma ferramenta de construção de cardápios para o restaurante Chapa Quente. A ferramenta é necessária para simplificar a geração de cardápios, considerando restrições alimentares e a disponibilidade de ingredientes em estoque. Atualmente, a gestão das receitas e do estoque do restaurante é ineficiente, sendo realizada por meio de arquivos CSV. A equipe fundadora do restaurante deseja melhorar esse processo.

## TECNOLOGIAS UTILIZADAS

- Python
- Estruturas de dados Dict e Set para implementar conceitos de Hashmaps
- Testes de software
- Orientação a objetos

## ARQUITETURA DO PROJETO

O projeto consiste em várias etapas:

1. **TESTANDO CLASSES JÁ IMPLEMENTADAS PARTE 1 E 2**: Nesta etapa, você implementará testes para as classes `Ingredient` e `Dish` que já foram parcialmente implementadas. Para a classe `Ingredient`, você garantirá que a classe pode ser instanciada corretamente e que os métodos mágicos funcionam conforme o esperado. Para a classe `Dish`, você testará a instância da classe, os métodos e garantirá que o dicionário de receita do prato forneça a quantidade correta de ingredientes.

2. **MAPEAMENTO PRATOS <> INGREDIENTES**: Você implementará a classe `MenuData`, que mapeia pratos e ingredientes com base em um arquivo CSV. Isso permitirá que o restaurante gerencie seus pratos e receitas de maneira mais eficaz. A classe será responsável por ler o arquivo CSV, instanciar pratos e ingredientes e criar um conjunto de pratos.

3. **GERAÇÃO DOS CARDÁPIOS**: A equipe anterior já começou a implementar a classe `MenuBuilder`, que interage com o cardápio e o estoque, permitindo a geração de cardápios com base em restrições alimentares. Sua tarefa é implementar o método `get_main_menu`, que retorna o cardápio completo ou um cardápio específico com base em restrições alimentares.

4. **ESTOQUE DE INGREDIENTES**: A gestão de estoque do restaurante é feita por meio de um arquivo CSV. Você deverá finalizar a implementação da classe `InventoryMapping`, que verifica a disponibilidade de receitas com base no estoque de ingredientes. Implemente os métodos `check_recipe_availability` e `consume_recipe` para verificar a disponibilidade de ingredientes e atualizar o estoque.

5. **CARDÁPIOS BASEADOS NO ESTOQUE**: Para tornar o cardápio ainda mais dinâmico, você complementará a implementação do método `get_main_menu` para considerar a disponibilidade em estoque dos ingredientes dos pratos, além das restrições alimentares. Isso garantirá que o cardápio reflita não apenas as preferências alimentares, mas também os ingredientes disponíveis no estoque.

## COMO EXECUTAR O PROJETO

1. Clone o repositório do projeto.
2. Certifique-se de ter o Python instalado em seu ambiente.
3. Execute os testes para as classes `Ingredient` e `Dish` para garantir que elas estejam funcionando corretamente.
4. Implemente a classe `MenuData` para mapear os pratos e ingredientes a partir do arquivo CSV.
5. Implemente o método `get_main_menu` na classe `MenuBuilder` para gerar cardápios com base em restrições alimentares e disponibilidade de estoque.
6. (Requisitos Bônus) Implemente a classe `InventoryMapping` para gerenciar o estoque de ingredientes e permitir a verificação de disponibilidade de receitas.

