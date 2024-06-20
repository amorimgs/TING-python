from ting_file_management.file_management import txt_importer
import sys


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
    if len(instance) == 0:
        return print("Não há elementos")
    remove = instance.dequeue()
    return print(f"Arquivo {remove['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if position < 0 or position > len(instance.data):
        return sys.stderr.write("Posição inválida")
    return print(instance.data[position])
