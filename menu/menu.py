import os
menu = ['Registrar Camper','Registrar Pruebas','Registrar area de entrenamiento','Crear Ruta de entrenamiento','Gestor de matricula','Consulta estudiante en riesgo','Reportes','Salir']
menuReporte = ['Campers Inscritos','Campers examen inicial aprobado','Trainers','Estudiantes con bajo rendimiento','Inscritos a ruta de entrenamiento','Desempeño Modulos por Ruta','Salir']

def menuPapl():
    header="""
    +++++++++++++++++++++++++++
    +   MENU - CAMPUSLANDS    +
    +++++++++++++++++++++++++++
    """    
    hasError = True
    print(header)
    for i,item in enumerate(menu):
        print(f'{(i+1)}. {item}')
    while hasError:
        try:
            return int(input(":) "))
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
            hasError = True

def menuRep():
    header="""
    +++++++++++++++++++++++++++++++
    +   REPORTES - CAMPUSLANDS    +
    +++++++++++++++++++++++++++++++
    """    
    hasError = True
    print(header)
    for i,item in enumerate(menuReporte):
        print(f'{(i+1)}. {item}')
    while hasError:
        try:
            return int(input(":) "))
        except ValueError:
            print("Error en el dato de ingreso, intente nuevamente")
            os.system("pause")
            hasError = True
