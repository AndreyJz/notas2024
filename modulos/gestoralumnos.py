import os
from tabulate import tabulate
alumno = {}
def AddStudent(alumnos:dict):
    id= input('Ingrese su Id: ')
    nombre = input('Ingrese el nombre: ')
    edad = int(input(f'Ingrese la edad de {nombre}: '))
    email = input(f'Ingrese el email de {nombre} : ')
    alumno = {
        'id':id,
        'nombre':nombre,
        'edad':edad,
        'email':email,
        'calificacion':{
            'parciales':[],
            'quizes':[],
            'trabajos':[]
        }
    }
    alumnos.update({id:alumno})
    print(alumnos)


def agregarParcial(alumnos:dict):
    id = (input('ingrese el Nro Id del estdiante: '))
    if ValidateStudent(alumnos,id):
        NotasParciales= int(input('ingrese las notas de parciales: '))
        alumnos[id]['calificacion']['parciales'].append(NotasParciales)
    else:
        print(f'El estudiante con id {id} no esta registrado')

def agregarQuizes(alumnos:dict):
    id = (input('ingrese el Nro Id del estdiante: '))
    if ValidateStudent(alumnos,id):
        NotasQuizes= int(input('ingrese las notas de quizes: '))
        alumnos[id]['calificacion']['quizes'].append(NotasQuizes)
    else:
        print(f'El estudiante con id {id} no esta registrado')
    
def agregarTrabajos(alumnos:dict):
    id = (input('ingrese el Nro Id del estdiante: '))
    if (ValidateStudent(alumnos,id)):
        NotasTrabajos= int(input('ingrese las notas de trabajos: '))
        alumnos[id]['calificacion']['trabajos'].append(NotasTrabajos)
    else:
        print(f'El estudiante con id {id} no esta registrado')


def SearchStudent(alumnos:dict):
    id = input('ingrese el Nro Id del estdiante: ')
    data = alumnos.get(id,False)
    if(type(data) == dict):
        print(data)
    elif((type(data) == bool) and (data == False)):
        print('El estudiante no se encuentra registrado')

info=[]
def ListData(alumnos:dict):
    for key,value in alumnos.items():
        info.append(value)
    print(tabulate(info,headers='keys',tablefmt='grind'))

def ValidateStudent(alumnos:dict,id)-> bool:
    return bool(alumnos.get(id,''))

def DelStudent(alumnos:dict):
    id = input('ingrese el Nro Id del estdiante: ')
    if (ValidateStudent(alumnos,id)):
        alumnos.pop(id)
    else:
        print(f'El estudiante con id {id} no esta registrado')

def DelByName(alumnos:dict):
    nombre = input('ingrese el Nombre del estdiante: ')
    for llave,valor in alumnos.items():
        if (nombre in valor['nombre']): 
            alumnos.pop(llave)
            break

