# Dataset dos Oscars

## Descrição

Dataset com os dados demográficos dos vencedores do Oscar em categorias selecionadas:

- Best Actress
- Best Supporting Actor
- Best Supporting Actress
- Best Director

## Dicionário de dados (em inglês)

| **Coluna** | **Nome**                      | **Valores Não Nulos** | **Tipo** | **Descrição**                             |
| ---------- | ----------------------------- | --------------------- | -------- | ----------------------------------------- |
| 0          | \_unit_id                     | 441 non-null          | int64    | Identificador                             |
| 1          | \_golden                      | 441 non-null          | bool     |                                           |
| 2          | \_unit_state                  | 441 non-null          | object   |                                           |
| 3          | \_trusted_judgments           | 441 non-null          | int64    |                                           |
| 4          | \_last_judgment_at            | 416 non-null          | object   |                                           |
| 5          | birthplace                    | 441 non-null          | object   | Local de Nascimento                       |
| 6          | birthplace:confidence         | 441 non-null          | float64  | Nível de Confiança do Local de Nascimento |
| 7          | date_of_birth                 | 441 non-null          | object   | Data de Nascimento                        |
| 8          | date_of_birth:confidence      | 441 non-null          | float64  | Nível de Confiança da Data de Nascimento  |
| 9          | race_ethnicity                | 441 non-null          | object   | Etnia                                     |
| 10         | race_ethnicity:confidence     | 441 non-null          | float64  | Nível de Confiança da Etnia               |
| 11         | religion                      | 441 non-null          | object   | Religião                                  |
| 12         | religion:confidence           | 441 non-null          | float64  | Nível de Confiança da Religião            |
| 13         | sexual_orientation            | 441 non-null          | object   | Orientação Sexual                         |
| 14         | sexual_orientation:confidence | 441 non-null          | float64  | Nível de Confiança da Orientação Sexual   |
| 15         | year_of_award                 | 441 non-null          | int64    | Ano do prêmio                             |
| 16         | year_of_award:confidence      | 441 non-null          | float64  | Nível de Confiança do Ano do prêmio       |
| 17         | award                         | 441 non-null          | object   | Tipo do Prêmio                            |
| 18         | biourl                        | 441 non-null          | object   | URL da Bio                                |
| 19         | birthplace_gold               | 9 non-null            | object   |                                           |
| 20         | date_of_birth_gold            | 8 non-null            | object   |                                           |
| 21         | movie                         | 441 non-null          | object   | Filme Ganhador do Prêmio                  |
| 22         | person                        | 441 non-null          | object   | Pessoa                                    |
| 23         | race_ethnicity_gold           | 2 non-null            | object   |                                           |
| 24         | religion_gold                 | 10 non-null           | object   |                                           |
| 25         | sexual_orientation_gold       | 3 non-null            | object   |                                           |
| 26         | year_of_award_gold            | 11 non-null           | float64  |                                           |

## Atribuição

| Atributo | Valor                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------ |
| Fonte    | [Kaggle](https://www.kaggle.com/datasets/fmejia21/demographics-of-academy-awards-oscars-winners) |
| Autor    | Felix Mejia (Owner)                                                                              |
| Licença  | CC0: Public Domain                                                                               |
