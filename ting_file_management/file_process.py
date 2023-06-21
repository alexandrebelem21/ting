import sys
from queue import Queue
from file_management import txt_importer


def process(path_file, instance):
    file_name = path_file.split('/')[-1]

    for item in instance.items:
        if item['nome_do_arquivo'] == file_name:
            return

    lines = txt_importer(path_file)

    if lines:
        file_data = {
            "nome_do_arquivo": file_name,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }
        instance.enqueue(file_data)

        print(file_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
