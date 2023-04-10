import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file_content = txt_importer(path_file)
    obj_instance = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_content),
        "linhas_do_arquivo": file_content,
    }
    instance.enqueue(obj_instance)
    print(obj_instance, file=sys.stdout)


def remove(instance):
    path_file = instance.search(0)["nome_do_arquivo"]
    content = instance.dequeue()
    if content is None:
        print("Não há elementos", file=sys.stdout)
    else:
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        infos = instance.search(position)
        print(infos, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stdout)
