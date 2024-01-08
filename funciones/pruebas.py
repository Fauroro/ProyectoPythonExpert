import os
import funciones.maincamper as mc
import funciones.camper as c
valor=0

def validNota(valor,txt,tipo):
    isActive = True
    while isActive:
        try:
            valid = c.validar(valor,txt,tipo)
        except ValueError:
            print("Error en el dato de ingreso")
        else:
            if (100>valid>0):
                return valid
            else:
                print("valor de la nota fuera de rango")


def regPrueba():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    valor = 0
    id=input('Ingrese el Nro Id del Camper:')
    data = mc.searchCamper(id)
    if len(data):
        if data["Estado"]=="Inscrito":
            notaTeo = validNota(valor,"Nota prueba teorica (entre 0 - 100)",float)
            notaPrac = validNota(valor,"Nota prueba Practica (entre 0 - 100)",float)
            nota = (notaPrac+notaTeo)/2
            if nota<60:
                estado = "Reprobado"
            else:
                estado = "Aprobado"
            data.update({"Estado":estado})
# cargar pruebas para matriculados
    else:
        print("no se encuentra el ID")
        os.system("pause")
    mc.campus["campus"]["campers"][id].update(data)
    mc.cf.NewFile(mc.campus)