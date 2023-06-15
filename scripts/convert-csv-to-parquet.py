# -*- coding: utf-8 -*-
import pandas as pd
import typer

app = typer.Typer()


@app.command()
def convert(csv_name: str, parquet_name: str = "output.parquet"):
    df = pd.read_csv(csv_name)
    df.to_parquet(parquet_name)


if __name__ == "__main__":
    app()
