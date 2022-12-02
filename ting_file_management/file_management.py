import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    with open(path_file, mode="r", encoding="utf-8") as file:
        return file.read().split("\n")
