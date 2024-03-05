import os

titulo="""
    +---------------------------+
    |   NOTAS ALUMNOS CAMPUS    |
    +---------------------------+
"""
def menu():
    lstOpciones = [1, 2, 3, 4, 5, 6]
    opciones = ['1. Agregar Estudiante', '2. Buscar Estudiante', '3. Lista Estudiantes', '4. Agregar Notas', '5. Eliminar Estudiante', '6. Salir']
    os.system('cls')
    print(titulo)
    for item in opciones:
        try:
            opciones = '1. Agregar Estudiante\n2. Buscar Estudiante\n3. Lista Estudiantes\n4. Agregar Notas\n5. Eliminar Estudiante\n6. Salir'
            print(opciones)
            op = int(input('_'))
            if (op not in lstOpciones):
                menu() 
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            menu() 
        else:
            return op

tituloGrades ='''
    +---------------------------+
    |   AGREGAR NOTAS CAMPUS    |
    +---------------------------+
'''

def menuGrades():
    lstOpciones = [1, 2, 3, 4]
    opciones = ['1. Agregar Parcial', '2. Agregar Quizes', '3. Agregar Trabajos', '4. Salir al Menu']
    os.system('cls')
    print(tituloGrades)
    for item in opciones:
        try:
            opciones = '1. Agregar Parcial\n2. Agregar Quizes\n3. Agregar Trabajos\n4. Salir al Menu'
            print(opciones)
            opG = int(input('_'))
            if (opG not in lstOpciones):
                menuGrades() 
        except ValueError:
            print('Dato invalido')
            os.system('pause')
            menuGrades() 
        else:
            return opG