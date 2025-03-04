from abc import ABC, abstractmethod
from datetime import datetime
from textwrap import dedent
import math

#Clases abstractas
class Persona(ABC):
    def __init__(self, id, nombre, telefono, direccion):
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
        self._direccion = direccion
     
    @abstractmethod   
    def mostrarInformacion(self):
        pass
    
class Mascota(ABC):
    def __init__(self, id, nombre, especie, raza, edad):
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self._historialCitas = []
    
    @abstractmethod
    def agregarAlHistorial(self):
        pass
    
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self._fecha = fecha
        self._hora = hora
        self._servicio = servicio
        self._veterinario = veterinario
        
    @abstractmethod
    def actualizar(self, **kwargs):
        pass
    
#Definicion de subclases
class Cliente(Persona):
    def __init__(self, id, nombre, telefono, direccion):
        super().__init__(id, nombre, telefono, direccion)
        self._mascotas = []
        
    def agregarMascota(self, mascota):
        self._mascotas.append(mascota)
                   
        
    def mostrarInformacion(self):
        infoCliente = dedent(f"""
        Id: {self._id}
        Nombre del cliente: {self._nombre}
        Telefono: {self._telefono}
        Direccion: {self._direccion}
        """)
        
        if not self._mascotas:
            infoCliente += "Mascotas: El cliente por el momento no tiene mascostas registradas\n"
        else:
            for i, mascota in enumerate(self._mascotas, start=1):
                infoCliente += dedent(f"""
                Mascota # {i}
                Nombre de la mascota: {mascota._nombre}
                Especie: {mascota._especie}
                Raza: {mascota._raza}
                Edad: {mascota._edad}
                """)
        
        return infoCliente
        
class Veterinario(Persona):
    def __init__(self, id, nombre, telefono, direccion, especialidad):
        super().__init__(id, nombre, telefono, direccion) 
        self._especialidad = especialidad
        
    def mostrarInformacion(self):
        return dedent(f"""
        Id: {self._id}
        Nombre del veterinario: {self._nombre}
        Telefono: {self._telefono}
        Direccion: {self._direccion}
        Especialidad: {self._especialidad}
        """)
        
class GestionMascota(Mascota):
    def agregarAlHistorial(self, citaProgramada):
        self._historialCitas.append(citaProgramada)
        
    def obtenerHistorial(self):
        return self._historialCitas
    
class GestionCita(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)          

class GestionVeterinaria:           
    
    @staticmethod    
    def registrarCliente(clientes):
        while True:
            print()
            print("#"*30)
            print("MODULO DE REGISTRO DE CLIENTE")
            print("#"*30)
            try:
                id = len(clientes) + 1
                nombre = input("\nIngrese el nombre del cliente: ").strip()
                telefono = input("Ingrese el telefono del cliente: ").strip()
                direccion = input("Ingrese la dirección del cliente: ").strip()
            
                if not nombre or not telefono or not direccion:
                    raise ValueError("\nTodos los campos son obligatorios. Por favor intente de nuevo")

                cliente = Cliente(id, nombre, telefono, direccion)
                clientes.append(cliente)
                print("\nCliente registrado exitosamente.")
                input("Presione <Enter> para continuar")
                break
                
            except ValueError as e:
                print(f"\nError: {e}")
                input("Presione <Enter> para continuar")
                
    @staticmethod
    def mostrarClientes(clientes):
        print()
        print("#"*30)
        print("MODULO DE VISUALIZACIÓN DE CLIENTE")
        print("#"*30)
        
        if not clientes:
            print("\nNo hay clientes registrados actualmente.")    

            
        else:
            for cliente in clientes:
                print(cliente.mostrarInformacion())   
        
        input("Presione <Enter> para continuar")
        
    
    @staticmethod        
    def actualizarCliente(clientes):
        print()
        print("#"*30)
        print("MODULO DE ACTUALIZACIÓN DE CLIENTE")
        print("#"*30)
        
        if not clientes:
            print("\nNo hay clientes registrados actualmente.")
            input("Presione <Enter> para continuar")
            return
                
        while True:
            try:
                idCliente = int(input("\nIngrese el número de id del cliente: ").strip())                        
            except ValueError:
                print("\nEl tipo de dato ingresado es invalido. Por favor intente de nuevo.")
                continue
            
            cliente_a_modificar = next((c for c in clientes if c._id == idCliente), None)
                     
            if cliente_a_modificar is None:
                print(f"\nNo existe un cliente con el ID {idCliente}. Por favor intente de nuevo.")
                continue
            
            break

        nuevoNombre = input("\nPor favor actualice el nombre: ").strip() or cliente_a_modificar._nombre     
        nuevoTelefono = input("Por favor actualice el telefono: ").strip() or cliente_a_modificar._telefono            
        nuevaDireccion = input("Por favor actualice la direccion: ").strip() or cliente_a_modificar._direccion
        
        cliente_a_modificar._nombre = nuevoNombre
        cliente_a_modificar._telefono = nuevoTelefono
        cliente_a_modificar._direccion = nuevaDireccion 
         
        print("\nCliente actualizado exitosamente.")    
        input("Presione <Enter> para continuar")
             
            
    @staticmethod        
    def registrarVeterinario(veterinarios):
        while True:
            print()
            print("#"*30)
            print("MODULO DE REGISTRO DE VETERINARIO")
            print("#"*30)
            try:
                id = len(veterinarios) + 1
                nombre = input("\nIngrese el nombre del veterinario: ").strip()
                telefono = input("Ingrese el telefono del veterinario: ").strip()
                direccion = input("Ingrese la direccion del veterinario: ").strip()
                especialidad = input("Ingrese la especialidad del veterinario: ").strip().upper()
            
                if not nombre or not telefono or not direccion or not especialidad:
                    raise ValueError("\nTodos los campos son obligatorios. Por favor intente de nuevo")

                veterinario = Veterinario(id, nombre, telefono, direccion, especialidad)
                veterinarios.append(veterinario)
                print("\nVeterinario registrado exitosamente.")
                input("Presione <Enter> para continuar")
                break
                
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione <Enter> para continuar")
                
                
    @staticmethod
    def mostrarVeterinarios(veterinarios):
        print()
        print("#"*30)
        print("MODULO DE VISUALIZACIÓN DE VETERINARIOS")
        print("#"*30)
        
        if not veterinarios:
            print("\nNo hay veterinarios registrados actualmente.")    
            
        else:
            for veterinario in veterinarios:
                print(veterinario.mostrarInformacion())   
        
        input("Presione <Enter> para continuar")
     
    @staticmethod           
    def actualizarVeterinario(veterinarios):
        print()
        print("#"*30)
        print("MODULO DE ACTUALIZACIÓN DE VETERINARIO")
        print("#"*30)
        
        if not veterinarios:
            print("\nNo hay veterinarios registrados actualmente.")
            input("Presione <Enter> para continuar")
            return            
        
        while True:
            try:
                idVeterinario = int(input("\nIngrese el número de id del veterinario: ").strip())                       
            except ValueError:
                print("\nEl tipo de dato ingresado es invalido. Por favor intente de nuevo.")
                    
            veterinario_a_modificar = next((v for v in veterinarios if v._id == idVeterinario), None)
            
            if veterinario_a_modificar is None:
                print(f"\nNo existe un veterinario con el ID {idVeterinario}. Por favor intente de nuevo.")
                continue
            
            break

        nuevoNombre = input("\nPor favor actualice el nombre: ").strip() or veterinario_a_modificar._nombre            
        nuevoTelefono = input("Por favor actualice el telefono: ").strip() or veterinario_a_modificar._telefono       
        nuevaDireccion = input("Por favor actualice la direccion: ").strip() or veterinario_a_modificar._direccion
                
        veterinario_a_modificar._nombre = nuevoNombre
        veterinario_a_modificar._tele = nuevoNombre
        veterinario_a_modificar._nombre = nuevoNombre
        
        print("\nVeterinario actualizado exitosamente.") 
        input("Presione <Enter> para continuar")
        
    
    @staticmethod
    def registrarMascota(clientes):
        while True:
            print()
            print("#"*30)
            print("MODULO DE REGISTRO DE MASCOTA")
            print("#"*30)
            
            if not clientes:
                print("\nNo hay clientes registrados actualmente. No es posible registrar mascotas.")
                input("Presione <Enter> para continuar")
                return
            
            try:
                idCliente = int(input("\nIngrese el id del cliente dueño de la mascota: ").strip())
                cliente = next((c for c in clientes if idCliente == c._id), None)
              
                if not cliente:
                    raise ValueError(f"No existe un cliente con el ID {idCliente}. Por favor intente nuevamente.")

                while True:
                    try:
                        nroMascotas = int(input("¿Cuantas mascotas desea registrar? (Puede registrar maximo 3 por intento): ").strip())
                        if nroMascotas <= 0 or nroMascotas > 3:
                            raise ValueError(f"El número ingresado no es valido. Por favor intente de nuevo.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")                

                for i in range(nroMascotas):
                    while True:
                        print(f"\nRegistre la mascota #{i+1}")
                        try:
                            id = len(cliente._mascotas) + 1
                            nombre = input("Ingrese el nombre de la mascota: ").strip()
                            especie = input("Ingrese la especie de la mascota: ").strip()
                            raza = input("Ingrese la raza de la mascota: ").strip()
                            edad = int(input("Ingrese la edad de la mascota: ").strip())
                            
                            if not nombre or not especie or not raza or edad < 0:
                                raise ValueError("Todos los campos son obligatorios. Por favor intente de nuevo.")
                            break
                        except ValueError as e:
                            print(f"\nError: {e}")
                    
                    mascota = GestionMascota(id, nombre, especie, raza, edad)
                    cliente.agregarMascota(mascota)
                    
                print(f"\n{'Mascota registrada exitosamente.' if nroMascotas == 1 else 'Mascotas registradas exitosamente.'}")
                input("Presione <Enter> para continuar")
                break
                
              
            except ValueError as e:
                print(f"\nError: {e}")
                input("Presione <Enter> para continuar")
    
              
    @staticmethod
    def actualizarMascota(clientes):
        print()
        print("#"*30)
        print("MODULO DE ACTUALIZACIÓN DE MASCOTA")
        print("#"*30)
        
        if not clientes:
                print("No hay clientes registrados actualmente. No es posible actualizar datos de las mascotas.")
                input("Presione <Enter> para continuar")
                return
        
        try:
            idCliente = int(input("\nIngrese el id del cliente dueño de la mascota: ").strip())
            cliente = next((c for c in clientes if idCliente == c._id), None)
                            
            if not cliente:
                raise ValueError(f"No existe un cliente con el ID {idCliente}. Por favor intente nuevamente.")
            
            if not cliente._mascotas:
                raise ValueError(f"El cliente {cliente._nombre} no tiene mascotas registradas actualmente.")
            
            idMascota = int(input("Ingrese el id del cliente de la mascota: ").strip())
            
            mascota_a_modificar = next((m for m in cliente._mascotas if m._id == idMascota), None)                    
                
            if mascota_a_modificar is None:
                raise ValueError(f"El cliente {cliente._nombre} no tiene una mascota con el ID {idMascota}. Por favor intente nuevamente.")
            
            nuevoNombre = input("Por favor actualice el nombre:").strip() or mascota_a_modificar._nombre            
            nuevaEspecie = input("Por favor actualice la especie:").strip() or mascota_a_modificar._especie                  
            nuevaRaza = input("Por favor actualice la raza:").strip() or mascota_a_modificar._raza
                              
            nuevaEdad = input("Por favor actualice la edad: ").strip()
            nuevaEdad = int(nuevaEdad) if nuevaEdad.isdigit() else mascota_a_modificar._edad   
            
            mascota_a_modificar._nombre = nuevoNombre
            mascota_a_modificar._especie = nuevaEspecie
            mascota_a_modificar._raza = nuevaRaza
            mascota_a_modificar._edad = nuevaEdad
            
            print("\nMascota actualizada exitosamente.") 
            input("Presione <Enter> para continuar")                                            
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione <Enter> para continuar")
    
    
    @staticmethod
    def programarCita(clientes, veterinarios):
        print()
        print("#"*30)
        print("MODULO DE PROGRAMACIÓN DE CITAS")
        print("#"*30)
        
        if not clientes:
            print("\nNo hay clientes registrados actualmente. No es posible programar citas.")
            input("Presione <Enter> para continuar")
            return
        
        if not veterinarios:
            print("\nNo hay veterinarios registrados actualmente. No es posible programar citas.")
            input("Presione <Enter> para continuar")
            return
        
        try:
            idCliente = int(input("\nIngrese el id del cliente dueño de la mascota: ").strip())
        
            cliente = next((c for c in clientes if c._id == idCliente), None)
            if not cliente:
                raise ValueError(f"No existe un cliente con el ID {idCliente}. Por favor intente nuevamente.")
            
            if not cliente._mascotas:
                raise ValueError(f"El cliente {cliente._nombre} no tiene mascotas registradas actualmente.")
            
            idMascota = int(input("Ingrese el id de la mascota: ").strip())        
            mascota = next((m for m in cliente._mascotas if m._id == idMascota), None)
            
            if not mascota:
                raise ValueError(f"El cliente {cliente._nombre} no tiene una mascota con el ID {idMascota}. Por favor intente nuevamente.")
        
            
            while True:
                try:
                    fecha = input("\nIngrese la fecha de la cita (AAAA-MM-DD): ").strip()
                    datetime.strptime(fecha, "%Y-%m-%d")
                    break
                except ValueError:
                    print("\nFormato de fecha incorrecto. Debe usar el formato AAAA-MM-DD")
                    
            while True:
                try:
                    hora = input("\nIngrese la hora de la cita (HH:MM): ").strip()
                    datetime.strptime(hora, "%H:%M")
                    break
                except ValueError:
                    print("\nFormato de hora incorrecto. Debe usar el formato HH:MM.")
            
            while True:
                try:
                    servicio = input("\nIngrese el servicio deseado (Consulta, Vacunación, Cirugia, etc): ").strip().upper()
                                        
                    if not servicio:
                        raise ValueError("El campo servicio es obligatorio. Por favor intente de nuevo.")
                    
                    idVeterinario = int(input("Ingrese el id del veterinario a agendar: ").strip())
                    
                    veterinario = next((v for v in veterinarios if v._id == idVeterinario), None)
                    
                    if not veterinario:
                        raise ValueError(f"No existe un veterinario con el ID {idVeterinario}. Por favor intente de nuevo.")
        
                    if servicio != veterinario._especialidad:
                        raise ValueError(f"El veterinario {veterinario._nombre} no atiende el servicio seleccionado. Por favor intente de nuevo.")
                    
                    break
                except ValueError as e:
                  print(f"\nError: {e}")                    
            
            cita = GestionCita(fecha, hora, servicio, veterinario._nombre)
            mascota.agregarAlHistorial(cita)
            print("\n¡Cita agregada exitosamente!")
            input("Presione <Enter> para continuar")
    
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione <Enter> para continuar")
    
    @staticmethod        
    def actualizarCita(clientes, veterinarios):
        print()
        print("#"*30)
        print("MODULO DE ACTUALIZACIÓN DE CITAS")
        print("#"*30)
        
        if not clientes:
            print("\nNo hay clientes registrados actualmente. No es posible actualizar citas.")
            input("Presione <Enter> para continuar")
            return
        
        if not veterinarios:
            print("\nNo hay veterinarios registrados actualmente. No es posible actualizar citas.")
            input("Presione <Enter> para continuar")
            return
        
        try:
            idCliente = int(input("\nIngrese el id del cliente dueño de la mascota: ").strip())
            idMascota = int(input("Ingrese el id de la mascota: ").strip())
            
            cliente = next((c for c in clientes if c._id == idCliente), None)
            if not cliente:
                raise ValueError(f"No existe un cliente con el ID {idCliente}. Por favor intente nuevamente.")
            
            if not cliente._mascotas:
                raise ValueError(f"El cliente {cliente._nombre} no tiene mascotas registradas actualmente.")
            
            mascota = next((m for m in cliente._mascotas if m._id == idMascota), None)
            if not mascota:
                raise ValueError(f"El cliente no tiene una mascota con el ID {idMascota}. Por favor intente nuevamente.")
            
            if not mascota._historialCitas:
                raise ValueError("La mascota no tiene citas registradas actualmente.")
            
            print("\nEstas son las citas que tiene registrada la mascota:")
            for i, cita in enumerate (mascota._historialCitas, start=1):
                print(dedent(f"""
                    Cita #{i}
                    Fecha: {cita._fecha}
                    Hora: {cita._hora}
                    Servicio: {cita._servicio}
                    Veterinario: {cita._veterinario}
                """))
            
            while True:
                try:
                    indiceCita = int(input("Por favor ingrese el número de cita que desea actualizar: ").strip())  
                    if indiceCita < 1 or indiceCita > len(mascota._historialCitas):
                        raise ValueError("No hay una cita con el número ingresado. Por favor intente de nuevo.")
                    break
                except ValueError as e:
                    print(f"\nError: {e}")
                    
            cita_a_modificar = mascota._historialCitas[indiceCita - 1] 
            
            while True:
                try:
                    nuevaFecha = input("\nPor favor actualice la fecha de la cita (AAAA-MM-DD): ").strip() or cita._fecha
                    datetime.strptime(nuevaFecha, "%Y-%m-%d")
                    break
                except ValueError:
                    print("\nFormato de fecha incorrecto. Debe usar el formato AAAA-MM-DD")
            
            while True:
                try:
                    nuevaHora = input("\nPor favor actualice la hora de la cita (HH:MM): ").strip() or cita._hora
                    datetime.strptime(nuevaHora, "%H:%M")
                    break
                except ValueError:
                    print("\nFormato de hora incorrecto. Debe usar el formato HH:MM")
            
            while True:
                try:
                    nuevoServicio = input("\nPor favor actualice el servicio deseado (Consulta, Vacunación, Cirugia, etc): ").strip().upper() or cita._servicio
                    if not nuevoServicio:
                        raise ValueError("El campo servicio es obligatorio. Por favor intente de nuevo.")
                    
                    idVeterinario = int(input("Ingrese el id del veterinario a agendar: ").strip())
                
                    veterinario = next((v for v in veterinarios if v._id == idVeterinario), None)
            
                    if not veterinario:
                        raise ValueError(f"No existe un veterinario con el ID {idVeterinario}. Por favor intente de nuevo.")
                
                    if nuevoServicio != veterinario._especialidad:
                        raise ValueError(f"El veterinario {veterinario._nombre} no atiende el servicio seleccionado. Por favor intente de nuevo.")
                    
                    break
                except ValueError as e:
                    print(f"\nError: {e}")                
                
            cita_a_modificar.actualizar(fecha=nuevaFecha, hora=nuevaHora, servicio=nuevoServicio, veterinario=veterinario._nombre)
            print("\nCita actualizada exitosamente.") 
            input("Presione <Enter> para continuar")                 
            
        except ValueError as e:
            print(f"\nError: {e}")
            input("Presione <Enter> para continuar")
            