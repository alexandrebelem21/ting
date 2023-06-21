import sys
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
    if len(instance) == 0:
        print("Não há elementos")
    else:
        path_file = instance.dequeue()
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        print(file_info)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
