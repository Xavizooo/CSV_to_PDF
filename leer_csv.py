import csv

with open ("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    next(lector)
    for fila in lector:
        print(fila)