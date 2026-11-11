#Leer archivos .csv e imprimir cada linea en pantalla 

archivos = open("datos.csv", "r")

for dato in archivos:
    print(dato)

archivos.close()