from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue
import sys


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    lines = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    instance.enqueue(file_info)
    print(file_info)


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if not len(instance):
        return print("Não há elementos")
    info = instance.dequeue()
    print(f"Arquivo {info['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        info = instance.search(position)
        print(info)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
