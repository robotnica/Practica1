linea_punteada = "----"

print(linea_punteada*10 + "Practica 2" + linea_punteada*10)

# EJERCICIO 1

print("EJERCICIO 1")


# EJERCICIO 2

print(linea_punteada*15)
print("EJERCICIO 2")





text = """The constants defined in this module are:The constants defined in␣
,→this module are:
string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants␣
,→described below. This value is not locale-dependent.
string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not␣
,→locale-dependent and will not change.
string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not␣
,→locale-dependent and will not change.
"""

# lista con todas las palabras
words = text.lower().split()

# lista con la palabra con mas apariciones en el texto
# y su cantidad de apariciones
from collections import Counter
from pyexpat import native_encoding
cnt = Counter(words).most_common(1)
# print(cnt)

print(f"{cnt[0][0]} es la palabra con mas apariciones en el texto")


# EJERCICIO 3

print(linea_punteada*15)
print("EJERCICIO 3")


import string

def print_matches ( c , text):

    """ Reads through the words of the text and prints the words 
    that start with a given letter (remindless of caps)
    """

    cocient_words = list(set(text.split()))


    for word in cocient_words:
        if ( word.lower().startswith(c.lower())):
            print(word)


text = """ And the Raven, never flitting, still is sitting, still is sitting
On the pallid bust of Pallas just above my chamber door;
    And his eyes have all the seeming of a demons that is dreaming,
    And the lamp-light over him streaming throws his shadow on the floor;
And my soul from out that shadow that lies floating on the floor
            Shall be lifted—nevermore!

"""

# letter = input("Type a letter ")
letter = 'c'

if letter in string.ascii_letters:
    print_matches(letter,text)
else:
    print('You did not type a letter :( ')



# EJERCICIO 4

print(linea_punteada*15)
print("EJERCICIO 4")


articulo = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

# separar el titulo

# evaluarlo

# separar en oraciones, por punto

# separar cada oracion por palabras, por espacio

# contarlas
halves = articulo.split('resumen: ')

title = (halves[0]).replace(' título: ','').replace('\n','')

summary = (halves[1]).replace('\n','')



def evaluate_title(title):
    len_title = len(title.split(' '))
    if len_title <= 10:
        print('El titulo esta ok') 
    else:
        print('El titulo no esta ok')




cntt = Counter({'Facil de leer': 0, 'Aceptable de leer': 0, 'Difícil de leer': 0, 'Muy difícil': 0})



def how_many_words_per_ktg(summary,cntt):

    sentences = summary.split('.')

    for sen in sentences:
        len_sen = len(sen.split(' '))
        if len_sen in range(0,13):
            cntt['Facil de leer'] += 1
        elif len_sen in range(13,18):
            cntt['Aceptable de leer'] += 1
        elif len_sen in range(18,26):
            cntt['Difícil de leer'] += 1
        else:
            cntt['Muy difícil'] += 1
    print('Cantidad de oraciones ')
    for ktg in cntt:
        print( ktg + ' : ' + str(cntt[ktg]))

evaluate_title(title)
how_many_words_per_ktg(summary,cntt)

""" match len_sen:
            case len_sen if len_sen <= 12:
                text_counter['easy_read'] += 1
            case  len_sen if len_sen <= 17:
                text_counter['aceptable_read'] += 1
            case  len_sen if len_sen <= 25:
                text_counter['hard_read'] += 1
            case  len_sen if len_sen > 25:
                text_counter['very_hard_read'] += 1
"""

# EJERCICIO 5

print(linea_punteada*15)
print("EJERCICIO 5")

"""Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas.
"""
# phrase = input('Write a phrase')
phrase = 'The eyes chico , they never lie'
splitted_phrase = phrase.lower().split()
# word = input('Write a string')
word = 'CHICO'

phrase_counter = Counter(splitted_phrase)
times = phrase_counter[word.lower()]

print('The word < ' + word + ' > appears '+ str(times) + ' time\s in the phrase \' ' + phrase + ' \'')


# EJERCICIO 5

print(linea_punteada*15)
print('PARTE 2')
print(linea_punteada*15)
print("EJERCICIO 5")

"""cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
print("Ingresaste más de 10 carcateres")
cant = 0
for car in cadena:
if car == "@" or car == "!":
cant = cant + 1
if cant >= 1:
print("Ingresaste alguno de estos símbolos: @ o !" )
else:
print("Clave válida")
"""

# Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
# parte de una palabra ingresada

#¿Cómo podemos simplificarlo?

#cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
cadena = 'The Day BEGINS'
if not ('@' in cadena or '!' in cadena) and (len(cadena)<10):
    print("Clave válida")
else:
    print("Clave invalida")


# EJERCICIO 6

print(linea_punteada*15)
print("EJERCICIO 6")

# Dada una frase donde las palabras pueden estar repetidas e indistintamente en mayúsculas y
# minúsculas, imprimir una lista con todas las palabras sin repetir y en letra minúscula.
frase = """
Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría
automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar
un montón de archivos con fotos de una manera compleja. Tal vez quieras
escribir alguna pequeña base de datos personalizada, o una aplicación
especializada con interfaz gráfica, o UN juego simple.
"""
sin_repetir = list(set(frase.lower().replace(',','').replace('.','').split()))

print(sin_repetir)

# EJERCICIO 7

print(linea_punteada*15)
print("EJERCICIO 7")


"""7. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma
es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres
"""



# EJERCICIO 10

print(linea_punteada*15)
print("EJERCICIO 10")
"""import os
ruta = os.path.dirname(os.path.realpath('.'))
print(ruta)

ruta_completa = os.path.join(ruta,'HP\Documents\Informatica\Python\Practica_1','archivo.txt')
with open(ruta_completa,'r') as archivin:
    test = archivin.read()

"""

with open('nombres_1.txt','r',encoding = 'utf-8') as file_names:
    names = file_names.read()
with open('eval1.txt','r',encoding = 'utf-8') as file_1st_marks:
    marks1 = file_1st_marks.read()
with open('eval2.txt','r',encoding = 'utf-8') as file_2nd_marks:
    marks2 = file_2nd_marks.read()

def make_list(my_string):
    """ Transforma el string que recibe en una lista, sin saltos de linea ni comillas """
    return my_string.replace('\n','').replace("\'",'').split(',')
    


def make_list_of_students(names,marks1,marks2):
    """Genera una lista de tuplas. Cada tupla contiene (nombre del alumno, suma de notas)
    """
    students=[]
    index = 0
    for name in names:
        sum_of_grades = int(marks1[index]) + int(marks2[index])
        student = (name,sum_of_grades/2)
        students.append(student)
        index +=1
        
    
    return students


def compute_average(students):
    """ Calcula la nota total promedio de los estudiantes recibidos por parametro """
    
    total_sum = 0
    for student in students:
        total_sum += int(student[1])
    
    average = (total_sum / len(students))
    
    return average
    
def inform_below_average(students,average_mark):
    """ Recorre la lista de (estudiantes,notas) y se va guardando, localmente, una lista con nombres 
    de los estudiantes cuyas notas estan por debajo del promedio ingresado por parametro.
    Finalmente imprime en pantalla tal lista de nombres
    """
    
    below_average=[]
    for (name,mark) in students:
        if (mark < average_mark):
            below_average.append(name)
    
    print('Estudiantes con nota por debajo del promedio:')
    for student in below_average:
        print(student)
    
    
    
names = make_list(names)
marks1 = make_list(marks1)
marks2 = make_list(marks2)


students = make_list_of_students(names,marks1,marks2)
average_mark = compute_average(students)
inform_below_average(students,average_mark)



