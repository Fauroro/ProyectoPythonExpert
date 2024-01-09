import os
import json
import menu.menu as menu
import funciones.camper as c
import funciones.pruebas as p
import funciones.reportes as r
import funciones.trainer as t
import funciones.rutas as ru

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
                t.regTrainer()
            elif opMenu==4:
                ru.rutas() # falta terminarlo
            elif opMenu==5:
                c.modCamper()
            elif opMenu==6:
                flag = True
                os.system("cls")
                while flag:
                    try:
                        opRep = menu.menuRep()
                    except ValueError:
                        print("Error en el dato de ingreso, intente nuevamente")
                    else:                           
                        if opRep==1:
                            r.inscritos()
                        elif opRep==2:
                            r.aprobInic()
                        elif opRep==3:
                            r.listTrainer()
                        elif opRep==4:
                            r.camperRiesgo()
                        elif opRep==5:
                            r.listaRuta()
                        elif opRep==6:
                            r.desempRuta()
                        elif opRep==7:
                            flag = False
                        else:
                            print("Opcion seleccionada inexistente.") 
                            os.system("pause")                  
            elif opMenu==7:
                isActive = False
            else:
                print("Opcion seleccionada inexistente.") 
                os.system("pause")     
                os.system("cls")             