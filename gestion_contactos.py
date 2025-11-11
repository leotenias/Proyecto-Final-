def ver_contactos(contactos):
    if not contactos:
        print("No hay ningun contacto guardado")
    else:
        print ("------ LISTA DE CONTACTOS ------")
        for c in contactos:
            print("{c['nombre']} - {c['telefono']} - {c['email']}")
            print("----------------------------------------------------------------")

def agregar_contacto(contactos):
    nombre= input("Nombre: ")
    telefono= input("Telefono: ")
    email=("Email: ")
    #ACA VERIFICAMOS QUE EL CONTACTO NO SEA REPETIDO
    for c in contactos:
        if c["nombre"].lower()
            print("Contacto con nombre ya existente!!")
            return
    contactos.append ({"nombre":,nombre,"telefono":telefono,"email":email})
    print("Su contacto se guardó con éxito!!")

def buscar_contacto(contactos,nombre):
    for c in contactos:
        if c["nombre"].lower()==nombre.lower():
            print(f"📇 {c['nombre']} - {c['telefono']} - {c['email']}")
            return
        print("CONTACTO NO ENCONTRADO")

def eliminar_contacto(contactos, nombre):
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            contactos.remove(c)
            print("Contacto eliminado.")
            return
    print("ERROR,no existe este contacto.")
