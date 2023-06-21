from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    arq = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(arq)

    print(arq)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        path_file = instance.dequeue()
        print(
            f'Arquivo {path_file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(file_info)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
