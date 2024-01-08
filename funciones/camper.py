import os
import json
import funciones.maincamper as mc

campers ={}

def validar(valor,txt,tipo):
    valid = True
    while (valid):
        try:
            valor = tipo(input(f"Ingrese {txt} del camper: "))
        except ValueError:
            print("Error en el dato de ingreso, intente otra vez")
            os.system("pause")
        else:
            if tipo==str:
                if len(valor)==0:
                    print("Error en el dato de ingreso, intente otra vez") 
                else:
                    valid = False
            else:   
                if valor<=0:
                    print("Error en el dato de ingreso, intente otra vez")    
                else:
                    valid = False    
    return valor

def regCamper():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    valor = ""
    print("""
    DATOS DEL CAMPER
    """)
    id = validar(valor,"ID",str)
    nombre = validar(valor,"nombre",str)
    apellido= validar(valor,"apellidos",str)
    direccion = validar(valor,"direccion",str)
    nroTelCel = validar(valor,"teléfono celular", str)
    nroTelFijo = validar(valor, "teléfono fijo", str)
    os.system("cls")
    print("""
    DATOS DEL ACUDIENTE
    """)
    idAcudiente = validar(valor,"ID del acudiente",str)
    nombreAcudiente = validar(valor,"nombre del acudiente",str)
    telAcudiente = validar(valor,"número de teléfono del acudiente",str)

    camper = {
        "NroId" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Direccion" : direccion,
        "Acudiente" : {},
        "Telecontacto" : {},
        "Estado" : "Inscrito"
    }

    acudiente = {
        "id" : idAcudiente,
        "nrotel" : telAcudiente,
        "nombre" : nombreAcudiente
    }

    phoneCel = {
        "id" : str((len(camper["Telecontacto"]) + 1)),
        "nrotel" : nroTelCel
    }

    phoneFijo = {
        "id" : str((len(camper["Telecontacto"]) + 1)),
        "nrotel" : nroTelFijo
    }

    camper["Acudiente"].update({str((len(camper["Acudiente"]) + 1)).zfill(3) : acudiente})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3) : phoneCel})
    camper["Telecontacto"].update({str((len(camper["Telecontacto"]) + 1)).zfill(3) : phoneFijo})
    campers.update({id : camper})
    mc.newCamper(campers)

def modCamper():
    mc.cf.checkFile(mc.campus)
    trainer = {}
    valor = ""
    isActive = True
    header="""
    ++++++++++++++++++++++++++++++
    +    GESTOR DE MATRICULAS    +
    ++++++++++++++++++++++++++++++
    """    
    print(header)
    while isActive:
        print("1. Matricular Camper \n2. \n4. Salir")
        try:
            opcion = validar(valor,"opcion seleccionada",int)
        except ValueError:
            print("Error en el dato de ingreso")
        else:
            if opcion == 1:
                id = validar(valor,"ID del Trainer",str)
                nombre = validar(valor,"nombre completo del Trainer",str)
                nroCel = validar(valor,"teléfono celular del Trainer", str)
                trainer={
                    "id":id,
                    "nombre":nombre,
                    "nroCel":nroCel,
                    "ruta":{}
                }
                try:
                    mc.campus["campus"]["trainer"].update({id:trainer})                
                except KeyError:
                    mc.campus["campus"].update({"trainer":{id:trainer}})
                else:
                    mc.campus["campus"]["trainer"].update({id:trainer})
            elif opcion == 2:
                print("Ingrese el ID del Trainer: ")
                id = validar(valor,"ID del Trainer",str)

                # nombre = validar(valor,"nombre completo del Trainer",str)
                
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                isActive = False

    mc.cf.NewFile(mc.campus)
