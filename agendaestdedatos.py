def mostrar_menu():
    print("**" * 25)
    print("Bienvenido a la agenda telefónica. Elija una de las siguientes opciones:")
    print("**" * 25)
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")
    print("**" * 25)

def agregar_persona(agenda):
    dni = input("Ingrese el DNI: ")
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")

    persona = {
        "apellido": apellido,
        "nombre": nombre,
        "email": email,
        "telefono": telefono
    }

    agenda[dni] = persona
    print("Persona agregada exitosamente.")

def modificar_persona(agenda):
    dni = input("Ingrese el DNI de la persona que desea modificar: ")

    if dni in agenda:
        persona = agenda[dni]
        print("Datos actuales de la persona:")
        print(persona)

        opcion_modificar = input("¿Desea cambiar los demás campos de la persona? (s/n): ")

        if opcion_modificar.lower() == "s":
            apellido = input("Ingrese el nuevo apellido: ")
            nombre = input("Ingrese el nuevo nombre: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo número de teléfono: ")

            persona["apellido"] = apellido
            persona["nombre"] = nombre
            persona["email"] = email
            persona["telefono"] = telefono

            print("Persona modificada exitosamente.")
        else:
            print("No se realizaron cambios.")
    else:
        print("No se encontró ninguna persona con ese DNI.")

def eliminar_persona(agenda):
    dni = input("Ingrese el DNI de la persona que desea eliminar: ")

    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada exitosamente.")
    else:
        print("No se encontró ninguna persona con ese DNI.")

def mostrar_agenda(agenda):
    if agenda:
        print("Agenda:")
        for dni, persona in agenda.items():
            print(f"DNI: {dni}")
            print(f"Apellido: {persona['apellido']}")
            print(f"Nombre: {persona['nombre']}")
            print(f"Email: {persona['email']}")
            print(f"Teléfono: {persona['telefono']}")
            print("--------------------")
    else:
        print("La agenda está vacía.")

def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_persona(agenda)
        elif opcion == "2":
            modificar_persona(agenda)
        elif opcion == "3":
            eliminar_persona(agenda)
        elif opcion == "4":
            mostrar_agenda(agenda)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
