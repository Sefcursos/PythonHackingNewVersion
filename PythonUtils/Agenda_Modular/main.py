# CONTROL PRINCIPAL DEL PROGRAMA
from contacto import Contacto
import gestor_agenda as ga
import utilidades

while True:
    utilidades.mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        c = Contacto(nombre, telefono, email)
        ga.agregar_contacto(c)
        print("Contacto agregado.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ")
        resultados = ga.buscar_contacto(nombre)
        for c in resultados:
            print(c)
        if not resultados:
            print("No se encontró el contacto.")

    elif opcion == "3":
        nombre = input("Nombre a eliminar: ")
        ga.eliminar_contacto(nombre)
        print("Contacto eliminado.")

    elif opcion == "4":
        for c in ga.listar_contactos():
            print(c)

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")