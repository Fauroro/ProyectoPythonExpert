import os
import json
import menu.menu as menu
import funciones.camper as c
import funciones.pruebas as p
import funciones.reportes as r

if __name__=='__main__':
    isActive = True
    while isActive:
        os.system("cls")
        try:
            opMenu = menu.menuPapl()
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
        else:
            if opMenu==1:
                c.regCamper()
            elif opMenu==2:
                p.regPrueba()
            elif opMenu==3:
                pass
            elif opMenu==4:
                pass
            elif opMenu==5:
                pass
            elif opMenu==6:
                r.camperRiesgo()
            elif opMenu==7:
                flag = True
                os.system("cls")
                while flag:
                    try:
                        opRep = menu.menuRep()
                    except ValueError:
                        print("Error en el dato de ingreso, intente nuevamente")
                    else:                           
                        if opMenu==1:
                            pass
                        elif opMenu==2:
                            r.aprobInic()
                        elif opMenu==3:
                            pass
                        elif opMenu==4:
                            pass
                        elif opMenu==5:
                            pass
                        elif opMenu==6:
                            pass
                        elif opMenu==7:
                            flag = False
                        else:
                            print("Opcion seleccionada inexistente.") 
                            os.system("pause")                  
            elif opMenu==8:
                isActive = False
            else:
                print("Opcion seleccionada inexistente.") 
                os.system("pause")                  