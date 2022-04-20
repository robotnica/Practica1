with open('nombres_1.txt','r',encoding = 'utf-8') as file_names:
    names = file_names.read()
with open('eval1.txt','r',encoding = 'utf-8') as file_1st_marks:
    marks1 = file_1st_marks.read()
with open('eval2.txt','r',encoding = 'utf-8') as file_2nd_marks:
    marks2 = file_2nd_marks.read()

def make_list(my_string):
    """ Transforma el string que recibe en una lista, sin saltos de linea ni comillas """
    return my_string.replace('\n','').replace("\'",'').split(',')

names = make_list(names)
marks1 = make_list(marks1)
marks2 = make_list(marks2)



def make_list_of_students(names,marks1,marks2):
    """Genera una lista de tuplas. Cada tupla contiene (nombre del alumno, suma de notas)
    """
    students=[]
    for index in range(len(names)):
        sum_of_grades = int(marks1[index]) + int(marks2[index])
        student = (names[index],sum_of_grades)
        students.append(student)
        
    
    return students

students = make_list_of_students(names,marks1,marks2)



def compute_average(students):
    """ Calcula la nota total promedio de los estudiantes recibidos por parametro """
    
    total_sum = 0
    total_of_students = len(students)
    for student in students:
        total_sum += int(student[1])
    
    average = total_sum / total_of_students
    
    return average

average_mark = compute_average(students)


def inform_below_average(students,average_mark):
    """ Recorre la lista de (estudiantes,notas) y se va guardando, localmente, una lista con nombres 
    de los estudiantes cuyas notas estan por debajo del promedio ingresado por parametro.
    Finalmente imprime en pantalla tal lista de nombres
    """
    
    below_average=[]
    for (name,sum_of_marks) in students:
        if (sum_of_marks < average_mark):
            below_average.append(name)
    
    print('Estudiantes con nota por debajo del promedio:')
    for student in below_average:
        print(student)
    
    
inform_below_average(students,average_mark)



# cambio 1 total_alumnos lo conozco es len(students)

# salio bien


# cambio 2: EN make_list_of_students(names,marks1,marks2): 
#listo calisto


