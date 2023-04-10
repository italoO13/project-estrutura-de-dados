def exists_word(word, instance):
    words = []
    for index in range(instance.__len__()):
        occ_in_file = []
        instance_content = instance.search(index)
        file_name = instance_content["nome_do_arquivo"]
        lines_file = instance_content["linhas_do_arquivo"]

        for n, line in enumerate(lines_file):
            if word.lower() in line.lower():
                occ_in_file.append({"linha": n + 1})

        if len(occ_in_file) > 0:
            words.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occ_in_file,
                }
            )
    return words


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
