""""Aqui vamos a crear el menu de opciones del usuario
 el cual va a poder selleccionar alguna opcion de la agenada"""

from sistema_agenda.gestion_contactos import (
ver_contactos, #Funcion para mostrar la lista completa de contactos
agregar_contacto,#Funcion para añadir un nuevo contacto a la lista
buscar_contacto,#Funcion para buscar un contacto por nombre
eliminar_contacto#Funcion para eliminar un contacto de la lista
)
from  sistema_agenda.gestion_archivos import(
cargar_contactos,
guardar_contactos

)
def main():
    contactos = cargar_contactos()
    while True:
        print("-----------------------AGENDA DE CONTACTOS-----------------------")
        print("1.Ver contactos")
        print("2.Agregar contacto")
        print ("3.Buscar contacto")
        print("4.Eliminar contacto")
        print("5.guardar y salir")

        opcion=input("Seleccione una opción: ")

        match opcion:
            case"1":
                ver_contactos(contactos)
            case"2":
                agregar_contacto(contactos)
            case"3":
                nombre=input("Ingrese el nombre que desea buscar: ")
                buscar_contacto(contactos,nombre)
            case"4":
                nombre=input("Ingrese el nombre que desea eliminar: ")
                eliminar_contacto(contactos,nombre)
            case"5":
                guardar_contactos(contactos)
                print("Saliendo...")
            break
        case_:
        print("ERROR,la opción no es válida")




