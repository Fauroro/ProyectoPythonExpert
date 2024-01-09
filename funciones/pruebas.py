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
    os.system("cls")
    header="""
    ++++++++++++++++++++++++++
    +   REGISTRAR PRUEBAS    +
    ++++++++++++++++++++++++++
    """    
    print(header)
    mc.cf.checkFile(mc.campus)
    valor = 0
    isActive = True
    while isActive:
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
                mc.campus["campus"]["campers"][id].update(data)
            elif data["Estado"]!="Reprobado":
                idModulo = 0
                notaTeo = validNota(valor,"Nota prueba teorica (entre 0 - 100)",float)
                notaPrac = validNota(valor,"Nota prueba Practica (entre 0 - 100)",float)
                notaTaller = validNota(valor,"Nota quices y trabajos (entre 0 - 100)",float)
                nota = notaPrac*0.6+notaTeo*0.3+notaTaller*0.1
                if nota<60:
                    estado = "Riesgo"
                    Estado = "Bajo Rendimiento"
                    data.update({"Estado":Estado})
                else:
                    estado = "Aprobado"
                    Estado = "Bajo Rendimiento"
                    data.update({"Estado":Estado})
                try: 
                    len(mc.campus["campus"]["pruebas"][id])
                except KeyError:
                    idModulo +=1
                else:
                    idModulo = len(mc.campus["campus"]["pruebas"][id]) + 1
                prueba = {
                    idModulo: {
                    "nota" : nota,
                    "estado": estado
                    }
                }
                pruebas = {
                    id:prueba
                }
                try: 
                    len(mc.campus["campus"]["pruebas"][id])
                except KeyError:
                    mc.campus["campus"]["pruebas"].update(pruebas)                
                else:
                    mc.campus["campus"]["pruebas"][id].update(prueba)                
            else:
                print("El Camper se encuentra Reprobado")
        else:
            print("no se encuentra el ID")
            os.system("pause")

        isActive=bool(input("Para registrar pruebas de otro camper Cualquier letra para continuar.... o Enter para finalizar "))
    mc.cf.NewFile(mc.campus)