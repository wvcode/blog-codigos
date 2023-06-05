# Dataset de Pokemons

## Descrição

Dataset com a listagem de todos os pokemons de cada geração, da primeira até a oitava.

Além dos dados demográficos, contém a matriz de eficiência do ataque de cada tipo de pokemon sobre este pokemon.

## Dicionário de dados (em inglês)

| **Coluna** | **Nome**                | **Valores Não-Nulo** | **Tipo de Dados** | **Descrição**                                    |
| ---------- | ----------------------- | -------------------- | ----------------- | ------------------------------------------------ |
| 0          | Number                  | 1032 non-null        | int64             | Número do Pokemon no Pokedex                     |
| 1          | Name                    | 1032 non-null        | object            | Nome do Pokemon                                  |
| 2          | Type 1                  | 1032 non-null        | object            | Tipo Primário                                    |
| 3          | Type 2                  | 548 non-null         | object            | Tipo Secundário                                  |
| 4          | Abilities               | 1032 non-null        | object            | Habilidades                                      |
| 5          | HP                      | 1032 non-null        | int64             | Pontos de Vida                                   |
| 6          | Att                     | 1032 non-null        | int64             | Status Base - Ataque                             |
| 7          | Def                     | 1032 non-null        | int64             | Status Base - Defesa                             |
| 8          | Spa                     | 1032 non-null        | int64             | Status Base - Ataque Especial                    |
| 9          | Spd                     | 1032 non-null        | int64             | Status Base - Defesa Especial                    |
| 10         | Spe                     | 1032 non-null        | int64             | Status Base - Velocidade                         |
| 11         | BST                     | 1032 non-null        | int64             | Soma de todos os Status Base                     |
| 12         | Mean                    | 1032 non-null        | float64           | Média de todos os Status Base                    |
| 13         | Standard Deviation      | 1032 non-null        | float64           | Desvio Padrão de todos os Status Base            |
| 14         | Generation              | 1032 non-null        | float64           | Geração                                          |
| 15         | Experience type         | 1032 non-null        | object            | Grupo de Experiência do Pokemon                  |
| 16         | Experience to level 100 | 1032 non-null        | int64             | Quantidade de Experiência para atingir Nível 100 |
| 17         | Final Evolution         | 1032 non-null        | float64           | Indicador de Evolução Final                      |
| 18         | Catch Rate              | 1032 non-null        | int64             | Taxa de Captura de Pokemon                       |
| 19         | Legendary               | 1032 non-null        | float64           | Indicador de Pokemon Lendário                    |
| 20         | Mega Evolution          | 1032 non-null        | float64           | Indicador de Mega Evolução                       |
| 21         | Alolan Form             | 1032 non-null        | float64           | Indicador de Forma Alolan                        |
| 22         | Galarian Form           | 1032 non-null        | float64           | Indicador de Forma Galarian                      |
| 23         | Against Normal          | 1032 non-null        | float64           |                                                  |
| 24         | Against Fire            | 1032 non-null        | float64           |                                                  |
| 25         | Against Water           | 1032 non-null        | float64           |                                                  |
| 26         | Against Electric        | 1032 non-null        | float64           |                                                  |
| 27         | Against Grass           | 1032 non-null        | float64           |                                                  |
| 28         | Against Ice             | 1032 non-null        | float64           |                                                  |
| 29         | Against Fighting        | 1032 non-null        | float64           |                                                  |
| 30         | Against Poison          | 1032 non-null        | float64           |                                                  |
| 31         | Against Ground          | 1032 non-null        | float64           |                                                  |
| 32         | Against Flying          | 1032 non-null        | float64           |                                                  |
| 33         | Against Psychic         | 1032 non-null        | float64           |                                                  |
| 34         | Against Bug             | 1032 non-null        | float64           |                                                  |
| 35         | Against Rock            | 1032 non-null        | float64           |                                                  |
| 36         | Against Ghost           | 1032 non-null        | float64           |                                                  |
| 37         | Against Dragon          | 1032 non-null        | float64           |                                                  |
| 38         | Against Dark            | 1032 non-null        | float64           |                                                  |
| 39         | Against Steel           | 1032 non-null        | float64           |                                                  |
| 40         | Against Fairy           | 1032 non-null        | float64           |                                                  |
| 41         | Height                  | 1032 non-null        | float64           | Altura em metros                                 |
| 42         | Weight                  | 1032 non-null        | float64           | Peso em quilos                                   |
| 43         | BMI                     | 1032 non-null        | float64           | Índice de Massa Corporal (Weight / Peso^2)       |

## Atribuição

| Atributo | Valor                                                                |
| -------- | -------------------------------------------------------------------- |
| Fonte    | [Kaggle](https://www.kaggle.com/datasets/maca11/all-pokemon-dataset) |
| Autor    | Mario Hernández (Owner)                                              |
| Licença  | CC0: Public Domain                                                   |
