from enum import Enum


class Options(Enum):
    EXISTS = 1
    SEARCH = 2


def aux_words(word, instance, opt: Options):
    words = []
    for index in range(instance.__len__()):
        occ_in_file = []
        instance_content = instance.search(index)
        file_name = instance_content["nome_do_arquivo"]
        lines_file = instance_content["linhas_do_arquivo"]

        occ_in_file = [
            {"linha": n + 1}
            for n, line in enumerate(lines_file)
            if word.lower() in line.lower() and opt == Options.EXISTS.value
        ]
        occ_in_file += [
            {"linha": n + 1, "conteudo": line}
            for n, line in enumerate(lines_file)
            if word.lower() in line.lower() and opt == Options.SEARCH.value
        ]

        if len(occ_in_file) > 0:
            words.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occ_in_file,
                }
            )
    return words


def exists_word(word, instance):
    return aux_words(word, instance, 1)


def search_by_word(word, instance):
    return aux_words(word, instance, 2)
