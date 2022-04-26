
import os

print('The current working directory is: ')
print(os.getcwd())



# te da el directorio desde el que estes trabajando
# cabe notar que, 'directorio actual desde el que estes..'
# PODRIA SER != la carpeta en qu esta guardado el .py

os.mkdir('New Directory')

ruta = os.path.dirname(os.path.realpath("."))

print('La ruta es:')
print(ruta)

# NO ENTIENDO os.path.join

# a ver

#path_arch = os.path.join(os.getcwd(), path_files)
#print(ruta)
