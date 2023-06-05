import pandas as pd

df = pd.read_csv("../datasets/stackoverflow/survey_results_public.csv")

# df.to_parquet("survey_results_public.parquet")


df2 = pd.read_parquet("survey_results_public.parquet")
