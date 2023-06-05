# Dataset de Salários de DS

## Descrição

Dataset com os dados de salários de data science ao longo dos anos, desde 2020.

## Dicionário de dados

| **Coluna**                     | **Descrição**                 | **Tipo de Dados** |         Valores          |              |              |                  |                    |                 |               |               |
| ------------------------------ | ----------------------------- | :---------------: | :----------------------: | :----------: | :----------: | :--------------: | :----------------: | :-------------: | :-----------: | :-----------: |
id | identificador único | inteiro 
work_year | ano de trabalho | inteiro
experience_level | nível de experiência | texto | EN - Entry-level(Junior) | MI - Mid-level(Pleno) | SE - Senior | EX - Executive-level / Director |
employment_type | Tipo de emprego | texto | PT Part-time | FT Full-time | CT Contract | FL Freelance |
job_title | Cargo | texto |
salary | Salário bruto na moeda do país | currency |
salary_currency | Moeda do salário | texto | 
salary_in_usd | Salário bruto em dólares | currency |
employee_residence | País de residência | texto |
remote_ratio | estilo da contratação | inteiro | 0 - No remote work (less than 20%) | 50 - Partially remote | 100 - Fully remote (more than 80%) | 
company_location | País da empresa ou filial contratando | texto
company_size | Tamanho da empresa | texto | S - less than 50 employees (small) | M - 50 to 250 employees (medium) | L - more than 250 employees (large) |


## Atribuição

| Atributo | Valor                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------ |
| Fonte    | [Kaggle](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries) |
| Autor    | Ruchi Bhatia (Owner)                                                                             |
| Licença  | CC0: Public Domain    