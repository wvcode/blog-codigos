# -*- coding: utf-8 -*-
import shutil
import typer
import os

app = typer.Typer()


@app.command()
def gather_pdfs(source_folder: str, output_folder: str = "inputs/pdfs"):
    files = []

    for del_filename in os.listdir(output_folder):
        os.remove(del_filename)

    for root, folders, filenames in os.walk(source_folder):
        for filename in filenames:
            if os.path.splitext(filename)[1] == ".pdf":
                files.append(os.path.join(root, filename))

    if len(files) > 0:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for item in files:
            newfilename = item.replace(source_folder + "/", "").replace("/", "-")
            shutil.copy2(item, os.path.join(output_folder, newfilename))


if __name__ == "__main__":
    app()
