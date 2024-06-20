from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    exist = False
    for inst in instance.data:
        if inst["nome_do_arquivo"] == path_file:
            exist = True

    if not exist:
        data = txt_importer(path_file)
        dataFormated = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }
        instance.enqueue(dataFormated)
        return print(dataFormated)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
