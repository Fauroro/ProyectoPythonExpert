import os
import funciones.maincamper as mc

def validar(valor,txt,tipo):
    valid = True
    while (valid):
        try:
            valor = tipo(input(f"Ingrese {txt}:"))
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

def regTrainer():
    mc.cf.checkFile(mc.campus)
    os.system("cls")
    trainer = {}
    valor = ""
    isActive = True
    while isActive:
        print("1. Registrar Trainer\n2. Asignar Horario y ruta\n3. Asignar Ruta\n4. Salir")
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
                    "ruta":{
                        "mañana":"",
                        "tarde":""
                    }
                }
                try:
                    mc.campus["campus"]["trainer"].update({id:trainer})                
                except KeyError:
                    mc.campus["campus"].update({"trainer":{id:trainer}})
                else:
                    mc.campus["campus"]["trainer"].update({id:trainer})
                mc.cf.NewFile(mc.campus)
                os.system("cls")
            elif opcion == 2:
                os.system("cls")
                isActiveTrainer = True
                if len(mc.campus["campus"]["trainer"])==0:
                    print("No se cuenta con Trainers Inscritos")
                    os.system("pause")
                    os.system("cls")
                    isActiveTrainer = False
                while isActiveTrainer:
                    id = validar(valor,"ID del Trainer",str)
                    try:
                        data = mc.campus["campus"]["trainer"][id]
                    except KeyError:
                        print("El Trainer no se encuentra registrado")
                    else: 
                        dataR = data.get("ruta")
                        print("Rutas Existentes")
                        rutas = mc.campus["campus"]["rutas"]
                        for i,items in rutas.items():
                            print(f"{i} - {items}")
                        for i,item in dataR.items():
                            print(f"Ruta inscrita en el horario de {i}: {item}")
                            if (bool(input(f"Desea editar la ruta de la {i} del Trainer {data['nombre']} Enter(Si)")) == False):
                                dataR[i] = input(f"Ingrese el codigo de la ruta para el Horario de {i}: ")
                            data["ruta"].update(dataR)
                        isActiveTrainer = False
                mc.campus["campus"]["trainer"][id].update(data)
                mc.cf.NewFile(mc.campus)
                os.system("cls") 


                
                
            elif opcion == 3:
                pass
            elif opcion == 4:
                isActive = False

    mc.cf.NewFile(mc.campus)