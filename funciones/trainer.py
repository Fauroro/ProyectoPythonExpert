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