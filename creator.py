import csv


'''
Parametros necesarios para crear el archivo
arr = nombre de la lista a iterar
name = nombre del archivo a crear
fieldnames = nombre de los campos de cabecera
options = se refiere a las opciones para ordenar los datos
'''


def file_creator(arr, name, fieldnames, options):
    with open(name, 'w', newline='') as file:
        fieldnames = fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in sorted(arr.items(), key=options):
            writer.writerow(v)
