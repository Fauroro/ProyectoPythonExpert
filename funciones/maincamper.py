import funciones.corefile as cf
import os
campus={
    "campus":{
        "campers":{},
        "rutas":{
            "manana":{
                "NodeJs":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "Java":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "NetCore":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                }
            },
            "tarde":{
                "NodeJs":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "Java":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                },
                "NetCore":{
                    "trainer":"",
                    "salon":"",
                    "campers":{}
                }
            }
        },
        "pruebas":{},
        "salones":{
            "Artemis":{
                "manana":"",
                "tarde":""
            },
            "Apolo":{
                "manana":"",
                "tarde":""
            },
            "Sputnik":{
                "manana":"",
                "tarde":""
            }
        },
        "trainer":{}
    }
}

cf.MY_DATABASE='data/campus.json'
def newCamper(campers : dict):
    campus["campus"]["campers"].update(campers)
    cf.AddData(campus)

def searchCamper(id)->dict:
    
    return campus.get("campus").get("campers").get(id,{})

def validarArchivoClientes():
    if(cf.checkFile()):
        print('ok')
        os.system('pause')
    else:
        cf.NewFile(campus)

# def delCustomer():
#     id=input('Ingrese el Nro Id a Borrar :')
#     cf.Eliminar(id,campus)

# def modifyCustomer(llave:str,cliente:dict):
#     for key,item in cliente.items():
#         if ((key != 'edad') and (key != 'cc')):
#             if (bool(input(f"Desea editar el campo {key} Enter(Si)")) == False):
#                 cliente[key]= input(f"Ingrese {key.capitalize()} del cliente : ")
#         elif key == 'edad':
#             validateAge = True
#             while (validateAge):
#                 try:
#                     cliente["edad"]= int(input(f"Ingrese {key.capitalize()}  del cliente : "))
#                 except ValueError:
#                     print("El valor ingresado es invalido")
#                 else:
#                     validateAge = False
#     campus[llave].update(cliente)
#     cf.NewFile(campus)
