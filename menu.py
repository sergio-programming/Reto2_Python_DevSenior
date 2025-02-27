from GestionVeterinaria import GestionVeterinaria
from textwrap import dedent

clientes = []
veterinarios = []


def menu():
    while True:
        print()
        print("#"*30)
        print("BIENVENIDO A LA PLATAFORMA DE HUELLA FELIZ")
        print("#"*30)
    
        print(dedent(f"""
                    1. Registrar clientes.
                    2. Ver información de clientes.
                    3. Actualizar información de clientes.
                    4. Registrar mascotas.
                    5. Actualizar información de mascotas.
                    6. Registrar veterinarios.
                    7. Ver información de veterinarios.
                    8. Actualizar información de veterinarios.
                    9. Programar cita de mascotas.
                    10. Actualizar cita de mascotas.
                    11. Salir.
                    """))
        
        try:
            opcion = int(input("Por favor ingrese una opción: ").strip())
        except ValueError:
            print("El tipo de dato ingresado no es valido. Por favor intente nuevamente")
            input("Presione <Enter> para continuar")
            continue
            
        if opcion == 1:
            GestionVeterinaria.registrarCliente(clientes)
        
        elif opcion == 2:
            GestionVeterinaria.mostrarClientes(clientes)
        
        elif opcion == 3:
            GestionVeterinaria.actualizarCliente(clientes)
        
        elif opcion == 4:
            GestionVeterinaria.registrarMascota(clientes)
        
        elif opcion == 5:
            GestionVeterinaria.actualizarMascota(clientes)
        
        elif opcion == 6:
            GestionVeterinaria.registrarVeterinario(veterinarios)
        
        elif opcion == 7:
            GestionVeterinaria.mostrarVeterinarios(veterinarios)
        
        elif opcion == 8:
            GestionVeterinaria.actualizarVeterinario(veterinarios)
        
        elif opcion == 9:
            GestionVeterinaria.programarCita(clientes, veterinarios)
        
        elif opcion == 10:
            GestionVeterinaria.actualizarCita(clientes, veterinarios)
        
        elif opcion == 11:
            print("Gracias por usar nuestra plataforma. Hasta pronto!!")
            break
        
        else:
            print("La opcion ingresada no es valida. Por favor intente nuevamente.")
            input("Presione <Enter> para continuar")