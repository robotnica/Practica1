texto = """ NumPy is the fundamental package for scientific computing with Python.

Website: https://www.numpy.org
Documentation: https://numpy.org/doc
Mailing list: https://mail.python.org/mailman/listinfo/numpy-discussion
Source code: https://github.com/numpy/numpy
Contributing: https://www.numpy.org/devdocs/dev/index.html
Bug reports: https://github.com/numpy/numpy/issues
Report a security vulnerability: https://tidelift.com/docs/security
It provides:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
Testing:

NumPy requires pytest and hypothesis. Tests can then be run after installation with:

python -c 'import numpy; numpy.test()'
Code of Conduct
NumPy is a community-driven open source project developed by a diverse group of contributors. The NumPy leadership has made a strong commitment to creating an open, inclusive, and positive community. Please read the NumPy Code of Conduct for guidance on how to interact with others in a way that makes our community thrive.

Call for Contributions
The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.

Writing code isn’t the only way to contribute to NumPy. You can also:

review pull requests
help us stay on top of new and old issues
develop tutorials, presentations, and other educational materials
maintain and improve our website
develop graphic design for our brand assets and promotional materials
translate website content
help with outreach and onboard new contributors
write grant proposals and help with other fundraising efforts
For more information about the ways you can contribute to NumPy, visit our website. If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invitation).

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.
"""
"""
texto_en_renglones = texto.split('\n') #es una lista

renglones_buscados = list(filter(lambda oracion : ('https' in oracion) or ('http' in oracion ), texto_en_renglones))

for renglon in renglones_buscados:
    print(renglon)


caracter = "g"
print(texto.split('\n')[2].endswith(caracter))

 for time in range(,3):
    word = input('Ingrese una palabra')
    if 'r' in (word):
        print(f" {word} tiene una letra r ")

print('\n') 

my_list = [2,4]
grade = int(input("Type a grade  "))
while (grade != 0):
    my_list.append(grade)
    grade = int(input("Type a grade  "))
print(my_list)

print('direccion de my_list:            ' + str(id(my_list)))


print(my_list*2)

print('direccion de my_list: repetida   ' + str(id(my_list)))

my_list=[] #creo un nuevo objeto en memoria
print('direccion de my_list: vacia      ' + str(id(my_list)))



word_1 = input('Write a word  ')
word_2 = input('Write a second word  ')

if (len(word_1) > len(word_2)):
    print(f"The word {word_1} is longer than the word {word_2}")
elif len(word_2) > len(word_1):
    print(f"The word {word_2} is longer than the word {word_1}")
else:
    print("Both are equally long")

for i in range(4):
    my_string = input('Ingrese una cadena:  ')
    print('La cadena tiene R ' if 'r' in my_string else 'La cadena NO tiene R ')


"""

lista = []
word = input('Type a word')
while (word != 'FIN'):
    lista.append(word)
    print(word[0:])
    print(word[:])
    print(word[:10])
    print(len(word)-1)
    word = input('Type a word')

for pal in lista:
    if (pal[0:1] == pal[-1:]):
        print(pal)
print(lista)

lista = [[1,2]] * 3
print(lista)

lista [0][1] = 'cambio'
print(lista)