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
    def __init__(self, nombre, especie, raza, edad):
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
        Nombre del cliente: {self._nombre}
        Telefono: {self._telefono}
        Direccion: {self._direccion}
        """)
        
        if not self._mascotas:
            infoCliente += "\nEl cliente por el momento no tiene mascostas registradas"
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
    def __init__(self):
        self.clientes = []
        self.veterinarios = []            
        
    def registrarCliente(self):
        while True:
            print()
            print("#"*30)
            print("MODULO DE REGISTRO DE CLIENTE")
            print("#"*30)
            try:
                id = len(self.clientes) + 1
                nombre = input("\nIngrese el nombre del cliente: ").strip()
                telefono = input("Ingrese el telefono del cliente: ").strip()
                direccion = input("Ingrese la dirección del cliente: ").strip()
            
                if not nombre or not telefono or not direccion:
                    raise ValueError("\nTodos los campos son obligatorios. Por favor intente de nuevo")

                cliente = Cliente(id, nombre, telefono, direccion)
                self.clientes.append(cliente)
                print("\nCliente registrado exitosamente.")
                input("Presione <Enter> para continuar")
                break
                
            except ValueError as e:
                print(f"\nError: {e}")
                input("Presione <Enter> para continuar")
            
    def actualizarCliente(self):
        cliente_a_modificar = None
        indice = 0
        while True:
            print()
            print("#"*30)
            print("MODULO DE ACTUALIZACIÓN DE CLIENTE")
            print("#"*30)
            while True:
                try:
                    idCliente = int(input("\nIngrese el número de id del cliente: ").strip())
                    break                        
                except ValueError:
                    print("\nEl tipo de dato ingresado es invalido. Por favor intente de nuevo.")
                        
            for i, cliente in enumerate(self.clientes):
                if cliente._id == idCliente:
                    cliente_a_modificar = cliente
                    indice = i
                    break
                
            if cliente_a_modificar is None:
                print(f"\nNo existe un cliente con el ID {idCliente}. Por favor intente de nuevo.")
                continue

            nuevoNombre = input("\nPor favor actualice el nombre: ").strip()
            if not nuevoNombre:
                nuevoNombre = cliente_a_modificar._nombre
                
            nuevoTelefono = input("Por favor actualice el telefono: ").strip()
            if not nuevoTelefono:
                nuevoTelefono = cliente_a_modificar._telefono
                    
            nuevaDireccion = input("Por favor actualice la direccion: ").strip()
            if not nuevaDireccion:
                nuevaDireccion = cliente_a_modificar._direccion
                    
            self.clientes[indice] = Cliente(idCliente, nuevoNombre, nuevoTelefono, nuevaDireccion)
            print("\nCliente actualizado exitosamente.") 
            input("Presione <Enter> para continuar")
            break  
            

    def registrarVeterinario(self):
        while True:
            print()
            print("#"*30)
            print("MODULO DE REGISTRO DE VETERINARIO")
            print("#"*30)
            try:
                id = len(self.veterinarios) + 1
                nombre = input("\nIngrese el nombre del veterinario: ").strip()
                telefono = input("Ingrese el telefono del veterinario: ").strip()
                direccion = input("Ingrese la direccion del veterinario: ").strip()
                especialidad = input("Ingrese la especialidad del veterinario: ").strip()
            
                if not nombre or not telefono or not direccion or not especialidad:
                    raise ValueError("\nTodos los campos son obligatorios. Por favor intente de nuevo")

                veterinario = Veterinario(id, nombre, telefono, direccion, especialidad)
                self.veterinarios.append(veterinario)
                print("\nVeterinario registrado exitosamente.")
                input("Presione <Enter> para continuar")
                break
                
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione <Enter> para continuar")
                
    def actualizarVeterinario(self):
        veterinario_a_modificar = None
        indice = 0
        while True:
            print()
            print("#"*30)
            print("MODULO DE ACTUALIZACIÓN DE VETERINARIO")
            print("#"*30)
            while True:
                try:
                    idVeterinario = int(input("\nIngrese el número de id del veterinario: ").strip())
                    break                        
                except ValueError:
                    print("\nEl tipo de dato ingresado es invalido. Por favor intente de nuevo.")
                        
            for i, veterinario in enumerate(self.veterinarios):
                if veterinario._id == idVeterinario:
                    veterinario_a_modificar = veterinario
                    indice = i
                    break
                
            if veterinario_a_modificar is None:
                print(f"\nNo existe un veterinario con el ID {idVeterinario}. Por favor intente de nuevo.")
                continue

            nuevoNombre = input("\nPor favor actualice el nombre: ").strip()
            if not nuevoNombre:
                nuevoNombre = veterinario_a_modificar._nombre
                
            nuevoTelefono = input("Por favor actualice el telefono: ").strip()
            if not nuevoTelefono:
                nuevoTelefono = veterinario_a_modificar._telefono
                    
            nuevaDireccion = input("Por favor actualice la direccion: ").strip()
            if not nuevaDireccion:
                nuevaDireccion = veterinario_a_modificar._direccion
                    
            nuevaEspecialidad = input("Por favor actualice la especialidad: ").strip()
            if not nuevaEspecialidad:
                nuevaEspecialidad = veterinario_a_modificar._especialidad
                    
            self.veterinarios[indice] = Veterinario(idVeterinario, nuevoNombre, nuevoTelefono, nuevaDireccion, nuevaEspecialidad)
            print("\nVeterinario actualizado exitosamente.") 
            input("Presione <Enter> para continuar")
            break
        
    def registrarMascota(self):
        while True:
            print()
            print("#"*30)
            print("MODULO DE REGISTRO DE MASCOTA")
            print("#"*30)
            
            try:
                idCliente = int(input("Ingrese el id del cliente dueño de la mascota: ").strip())
                cliente = next((c for c in self.clientes if idCliente == c._id), None)
              
                if not cliente:
                    raise ValueError(f"\nNo existe un cliente con el ID {idCliente}. Por favor intente nuevamente.")

                while True:
                    try:
                        nroMascotas = int(input("¿Cuantas mascotas desea registrar? (Puede registrar maximo 3 por intento): ").strip())
                        if nroMascotas <= 0 or nroMascotas > 3:
                            raise ValueError(f"El número ingresado no es valido. Por favor intente de nuevo.")
                        break
                    except ValueError as e:
                        print(f"Error: {e}")            

                for i in range(nroMascotas):
                    print(f"\nRegistre la mascota #{i+1}")
                    while True:
                        try:
                            nombre = input("Ingrese el nombre de la mascota: ").strip()
                            especie = input("Ingrese la especie de la mascota: ").strip()
                            raza = input("Ingrese la raza de la mascota: ").strip()
                            edad = int(input("Ingrese la edad de la mascota: ").strip())
                            
                            if not nombre or not especie or not raza or edad < 0:
                                raise ValueError("Todos los campos son obligatorios. Por favor intente de nuevo.")
                            break
                        except ValueError as e:
                            print(f"Error: {e}")
                    
                    mascota = GestionMascota(nombre, especie, raza, edad)
                    cliente.agregarMascota(mascota)
                    
                print(f"\n{'Mascota registrada exitosamente.' if nroMascotas == 1 else 'Mascotas registradas exitosamente.'}")
                input("Presione <Enter> para continuar")
                break
                
              
            except ValueError as e:
                print(f"\nError: {e}")
                input("Presione <Enter> para continuar")
              
    def programarCita(self):
        try:
            idCliente = int(input("Ingrese el id del cliente dueño de la mascota: ").strip())
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()
            
            cliente = next((c for c in self.clientes if c._id == idCliente), None)
            if not cliente:
                raise ValueError("Cliente no registrado. Por favor intente de nuevo.")
            
            mascota = next((m for m in self.cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no registrada. Por favor intente de nuevo.")
            
            while True:
                try:
                    fecha = input("\nIngrese la fecha de la cita (AAAA-MM-DD): ").strip()
                    hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
                    servicio = input("Ingrese el servicio deseado (Consulta, Vacunación, Cirugia, etc): ").strip()
                    idVeterinario = int(input("Ingrese el id del veterinario a agendar: ").strip())
                    
                    veterinario = next((v for v in self.veterinarios if v._id == idVeterinario), None)
                    
                    if not fecha or not hora or not servicio or not veterinario:
                        raise ValueError("Todos los campos son obligatorios. Por favor intente de nuevo.")
                    
                    if not veterinario:
                        raise ValueError(f"No existe un veterinario con el ID {idVeterinario}. Por favor intente de nuevo.")
                    
                    if servicio != veterinario._especialidad:
                        raise ValueError(f"El veterinario {veterinario._nombre} no atiende el servicio seleccionado. Por favor intente de nuevo.")
                    
                    break
                except ValueError as e:
                    print(f"\nError: {e}")
            
            
            
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            
            cita = GestionMascota(fecha, hora, servicio, veterinario)
            mascota.agregarAlHistorial(cita)
            print("\n¡Cita agregada exitosamente!")
        
        except ValueError as e:
            print(f"\nError: {e}")