def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        file_name = file["nome_do_arquivo"]

        arq = {
            'palavra': word,
            'arquivo': file_name,
            'ocorrencias': []
        }
        for line_index, line in enumerate(file['linhas_do_arquivo'], start=1):
            if word.lower() in line.lower():
                arq['ocorrencias'].append({'linha': line_index})
        if arq["ocorrencias"]:
            result.append(arq)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
