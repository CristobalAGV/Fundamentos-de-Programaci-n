import funcionesTarea as funcion
import time
flag1=True;
flag2=True;

while flag1:
    usuarios_registrados= {
        "cristobal_gv": "1234",
        "benja_g": "4321",
        "francis_vr": "1111"
    }
    usuario = input("Ingrese un nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if usuario in usuarios_registrados and contraseña == usuarios_registrados[usuario]:
        print(f"Inicio de sesion exitosa. ¡Bienvenido, @{usuario}!")
        print()
        while flag2:
            print("\n:::: MENÚ DE OPCIONES ::::\n")
            print("1.- Registrar trabajador.")
            print("2.- Listar todos los trabajadores.")
            print("3.- Imprimir planilla de sueldos.")
            print("4.- Salir del programa.")
            try:
                opcion=int(input("\nIngrese una opcion: "))
            except:
                print("Por favor ingrese una opciòn valida. Vuelva a intentarlo")
            else:
                if opcion == 1:
                    print("-- Registrar Trabajadores --\n")
                    funcion.registrar_usuario()
                elif opcion == 2:
                    print("-- Listado de Trabajadores --")
                    funcion.mostrar_trabajadores()
                elif opcion == 3:
                    print("-- Imnprimir planilla de Sueldo --")
                elif opcion == 4:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    break
                else:
                    print("Por favor ingrese una opción válida.")
    else:
        print("\nCredenciales invalidas. Por favor, vuelva a intentarlo.\n")

