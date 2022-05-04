## PROBANDO FUNCIONES Y PARAMETROS

def prueba (cod, guru, nombre = 'lola'):
    print(f"{nombre} es el nombre de mi gateto")
    print(f"ah y tambien se sumar {cod} + {guru} = {cod+guru} jaja mira como sumo")

prueba(34,56,'ana')

def prueba2 (juki, lope, nombre = 'caperucita'):
    print(f"{nombre} le decian a mi tio, nah mentira, mira si a mi tio le van a decir asi")
    print(f"te hago una suma? d1 {juki} + {lope} = {juki + lope} ,dnd")
    

prueba2(juki = 'pepa',lope = 'lolapaluza')


def prueba3 (*hoja):
    
    for arg in hoja:
        print(f"{arg} es un elemento de la tupla")

tuplea = ('lunar', 50)
prueba3(tuplea,3)

print('-'*10)

def imprimo(*args):
    """ Esta función imprime los argumentos y sus tipos"""
    for valor in args:
        print(f"{valor} es de tipo {type(valor)}")

imprimo(*tuplea)
imprimo('hola', 'chau')

print('\n'*2)
print('-'*10)

sandricito = { 'clave1': 'surprise','clave2': 'happybday'}

print(type(sandricito.items()))

def prueba4 (**kwargs):

    for clave,valor in kwargs.items():
        print(f" {clave} es la clave, {valor} es el valor")

prueba4(**sandricito)




print('-'*15)

texto = """ Wise man say only fools rush in """

def procesar_cadena(cadena):
    lista = cadena.split()
    lista = sorted(lista,key = lambda palabra: palabra.lower())
    print(lista)

if __name__ == "__main__":
    procesar_cadena(texto)


