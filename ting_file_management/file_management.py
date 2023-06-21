import sys


def txt_importer(file_path):
    if not file_path.endswith('.txt'):
        print("Formato inválido", file=sys.stderr)
        return []

    try:
        with open(file_path, 'r') as file:
            lines = file.read().split('\n')
            return lines
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado", file=sys.stderr)
        return []
