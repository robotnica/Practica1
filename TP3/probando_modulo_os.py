import os
import csv
ruta = os.path.dirname(os.path.realpath("."))
ruta_archivo = os.path.join(ruta,"netflix_titles.csv")


archivo = open(ruta_archivo, "r")
csvreader = csv.reader(archivo, delimiter=',')
print(type(csvreader))

encabezado = next(csvreader)
print(type(encabezado))
print(encabezado)
archivo.close()

print('*'*10)






