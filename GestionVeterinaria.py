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
        return dedent(f"""
        Nombre del cliente: {self._nombre}
        Telefono: {self._telefono}
        Direccion: {self._direccion}
        """)
        if not self._mascotas:
            print("El cliente por el momento no tiene mascostas registradas")
        else:
            for i, mascota in enumerate(self._mascotas, start=1):
                return dedent(f"""
                Mascota # {i}
                Nombre de la mascota: {mascota.nombre}
                Especie: {mascota.especie}
                Raza: {mascota.raza}
                edad: {mascota.edad}
                """)
        
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
    def agregarAlHistorial(self, detallesServicio):
        self._historialCitas.append(detallesServicio)
        
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
                direccion = input("Ingrese la d del cliente: ").strip()
            
                if not nombre or not telefono or not direccion:
                    raise ValueError("\nTodos los campos son obligatorios. Por favor intente de nuevo")

                cliente = Cliente(id, nombre, telefono, direccion)
                self.clientes.append(cliente)
                print("Cliente registrado exitosamente.")
                input("Presione <Enter> para continuar")
                break
                
            except ValueError as e:
                print(f"Error: {e}")
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
                print(f"\nNo existe un cliente con el ID {idCliente}. Por favor intente nuevamente.")
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
            print("Cliente actualizado exitosamente.") 
            input("Presione <Enter> para continuar")
            break  
            

