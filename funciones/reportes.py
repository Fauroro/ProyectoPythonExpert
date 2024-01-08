import os
import funciones.maincamper as mc


def camperRiesgo():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["pruebas"]
    cont = 0
    print("Estudiantes en riesgo en el ultimo modulo presentado: \n")
    print("ID\t\tNombre\t\tApellido\t\tModulo\n")
    for i,items in data.items():
        last = str(len(data[i].keys()))
        dataC = mc.searchCamper(i)
        if data[i][last]["estado"]=="Riesgo":
            print(f"{i}\t\t{dataC.get('Nombre')}\t\t{dataC.get('Apellido')}\t\tModulo {last}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers en riesgo en el ultimo modulo")
    print("")
    os.system("pause")




def aprobInic():
    os.system("cls")
    mc.cf.checkFile(mc.campus)
    data = mc.campus["campus"]["campers"]
    print("ID\t\tNombre\t\tApellido\n")
    cont = 0
    for i,items in data.items():
        if data.get("Estado")=="Aprobado":
            (f"{i}\t\t{data.get('Nombre')}\t\t{data.get('Apellido')}")
            cont +=1
    if cont == 0:
        os.system("cls")
        print("No se encuentran Campers con el examen incial aprobado")
    print("")
    os.system("pause")