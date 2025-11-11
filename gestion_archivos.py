def cargar_contactos(nombre_archivo="contactos.txt"):
    contactos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 3:
                    nombre, telefono, email = datos
                    contactos.append({
                        "nombre": nombre,
                        "telefono": telefono,
                        "email": email
                    })
    except FileNotFoundError:
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            pass
        print("📂 Archivo no encontrado. Se creó uno nuevo.")

    return contactos


def guardar_contactos(contactos, nombre_archivo="contactos.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for c in contactos:
            f.write(f"{c['nombre']},{c['telefono']},{c['email']}\n")

    print("Los contactos se han guardado correctamente :D.")

