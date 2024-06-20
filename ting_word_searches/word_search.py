def exists_word(word, instance):
    result = []
    for i in instance.data:
        ocorrencias = []
        for index in range(len(i["linhas_do_arquivo"])):
            if word.lower() in i["linhas_do_arquivo"][index].lower():
                ocorrencias.append({"linha": index + 1})
        if ocorrencias:
            result.append(
                {
                    "palavra": word,
                    "arquivo": i["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
