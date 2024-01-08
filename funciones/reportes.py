import os
import funciones.maincamper as mc

def inscritos():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    cont = 0
    print("Estudiantes en estado Inscrito: \n")
    print("ID\t\tNombre\t\tApellido\t\tEstado\n")
    for i,items in data.items():
        if data[i]["Estado"]=="Inscrito":
            print(f"{i}\t\t{data[i]['Nombre']}\t\t{data[i]['Apellido']}\t\t{data[i]['Estado']}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers en estado Inscrito")
    print("")
    os.system("pause")    
    os.system("cls")

def camperRiesgo():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    cont = 0
    print("Estudiantes en riesgo en el ultimo modulo presentado: \n")
    print("ID\t\tNombre\t\tApellido\t\tModulo\n")
    for i,items in data.items():
        dataC = mc.campus["campus"]["pruebas"][i]
        last = str(len(dataC.keys()))
        if data[i]["Estado"]=="Bajo Rendimiento":
            print(f"{i}\t\t{data.get(i).get('Nombre')}\t\t{data.get(i).get('Apellido')}\t\tModulo {last}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers en riesgo en el ultimo modulo")
    print("")
    os.system("pause")
    os.system("cls")

def listTrainer():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["trainer"]
    print("Trainers que se encuentran trabajando en Campuslands: \n")
    print("ID\t\tNombre\t\tApellido\n")
    if len(data.keys())==0:
        os.system("cls")
        print("No se encuentran Trainers registrados")
    else:
        for i,items in data.items():
            print(f"{i}\t\t{data[i]['nombre']}\t\t{data[i]['nroCel']}")
    print("")
    os.system("pause")
    os.system("cls")

def aprobInic():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    print("Estudiantes que aprobaron el examen inicial: \n")
    print("ID\t\tNombre\t\tApellido\t\tEstado\n")
    cont = 0
    for i,items in data.items():
        if data[i]["Estado"]=="Aprobado":
            print(f"{i}\t\t{data[i]['mombre']}\t\t{data[i]['Apellido']}\t\t{data[i]['Estado']}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers con el examen incial aprobado")
    print("")
    os.system("pause")

