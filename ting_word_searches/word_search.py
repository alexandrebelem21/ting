def exists_word(word, instance):
    my_occurrences = []
    my_word = word.lower()
    index = 0

    for element in instance.queue:
        for line in element["linhas_do_arquivo"]:
            if my_word in line.lower():
                index += 1
                my_occurrences.append({"linha": index})
            else:
                index += 1

    if len(my_occurrences) == 0:
        return []

    return [
        {
            "palavra": my_word,
            "arquivo": element["nome_do_arquivo"],
            "ocorrencias": my_occurrences,
        }
    ]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
