# -*- coding: utf-8 -*-

import csv
import os
import time
from typing import Annotated

import bs4
import openai
import typer
from dotenv import load_dotenv
from requests_html import HTMLSession

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = typer.Typer()


def retorna_lista(nomearquivo: str):
    html_artigos = bs4.BeautifulSoup(open(nomearquivo, "r"))
    list_artigos = html_artigos.find_all("li")

    artigos = []
    for item in list_artigos:
        record = {}
        record = {
            "titulo": item.a.text,
            "link": item.a["href"],
            "autores": None,
            "resumo": None,
            "categorias": None,
        }
        artigos.append(record)
    return artigos


def retorna_campos(registro: dict):
    seletor_autor = [
        "#root > div > div > div:nth-child(3) > div > article > div > div > section > div > div:nth-child(3) > div > div > div:nth-child(2) > div > div > div > div > div > div > div > span > div > div > div > div > div > p > a",
        "#root > div > div > div:nth-child(3) > div > article > div > div > section > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > div > div > div > div > div > span > div > div > div > div > div > p > a",
        "#root > div > div > div:nth-child(2) > div > article > div > div > section > div > div:nth-child(2) > div > div > div > div > div > div > div > div > div > div > span > div > div > div > div > div > p > a",
        "#root > div > div > div:nth-child(2) > div > article > div > div > section > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(2) > div > div > div > div > div > div > div > span > div > div > div > div > div > p > a",
    ]
    seletor_titulo_lead = [
        "#root > div > div > div:nth-child(3) > div > article > div > div > section > div > div:nth-child(3) > div > div > div:nth-child(2)",
        "#root > div > div > div:nth-child(2) > div > article > div > div > section > div > div:nth-child(3) > div:nth-child(1) > div > div:nth-child(2)",
    ]

    request = HTMLSession()
    try:
        print(registro["link"])
        conteudo_html = request.get(registro["link"])
        autor = "Not available"

        for item in seletor_autor:
            aux_autor = None
            aux_autor = conteudo_html.html.find(item, first=True)
            if aux_autor is not None:
                autor = aux_autor
                break

        head = "Not available"
        for item in seletor_titulo_lead:
            aux_head = None
            aux_head = conteudo_html.html.find(item, first=True)
            if aux_head:
                aux_lead = aux_head.find("h2", first=True)
                if aux_lead is not None:
                    head = aux_lead.text

        registro["autores"] = autor.text
        registro["resumo"] = head

        return True, registro
    except:
        print("URL {0} com erro. Verifique.".format(registro["link"]))
        return False, registro


def retorna_categorias(titulo, resumo):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"We have these categories: dbt, Python, DataViz, Tableau, PowerBI, and Generative AI. Given those categories, please classify the following text with those categories: {titulo} - {resumo}. You can use only the categories listed. You can classify with multiple categories. If you think that none of the categories applies, you can tag as Other.",
        temperature=0.2,
        max_tokens=20,
    )
    return response.choices[0].text.strip()


def save_file(arquivo, dados):
    folder, file = os.path.split(arquivo)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(arquivo, "w", encoding="utf-8") as fw:
        csvW = csv.DictWriter(
            fw, fieldnames=["titulo", "link", "autores", "resumo", "categorias"]
        )
        csvW.writeheader()
        csvW.writerows(dados)


@app.command()
def main(
    nomearquivo: str,
    output: str = "outputs/classified_data.csv",
    error: str = "outputs/error_data.csv",
    intermediate: str = "outputs/artigos_comp.csv",
    skip_load: Annotated[bool, typer.Option("--skip-load")] = False,
):
    if skip_load:
        artigos_comp = []
        with open(nomearquivo, "r", encoding="utf-8") as fr:
            csvR = csv.DictReader(fr)
            for item in csvR:
                artigos_comp.append(item)
    else:
        artigos_raw = retorna_lista(nomearquivo)

        artigos_comp = []
        artigos_erro = []
        for idx, item in enumerate(artigos_raw):
            success, record = retorna_campos(item)
            if success:
                artigos_comp.append(record)
            else:
                artigos_erro.append(record)

            if idx % 10 == 0:
                print(f"{idx+1} registros processados...")
                time.sleep(10)

        save_file(intermediate, artigos_comp)

        save_file(error, artigos_erro)

    lista_final = []
    for idx, item in enumerate(artigos_comp):
        item["categorias"] = retorna_categorias(item["titulo"], item["resumo"])
        lista_final.append(item)
        if idx % 10 == 0:
            print(f"{idx+1} registros categorizados...")
            time.sleep(10)
            if idx > 0:
                break

    save_file(output, lista_final)


if __name__ == "__main__":
    app()
