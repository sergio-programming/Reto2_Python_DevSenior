from abc import ABC, abstractmethod
from datetime import datetime
from textwrap import dedent

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
    
    @abstractmethod
    def registrar(self):
        pass
    
class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad, nombrePropietario):
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._edad = edad
        self._historialCitas = []
        
    @abstractmethod
    def actualizar(self):
        pass
    
    @abstractmethod
    def agregarAlHistorial(self):
        pass
    
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        self._fecha = fecha
        self._hora = hora
        self._servicio = servicio
        self._veterinario
        
    @abstractmethod
    def actualizarCita(self, **kwargs):
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
        Mascotas: {self._mascotas}
        """)
        
    

class GestionVeterinaria:
    def __init__(self):
        self.clientes = []
        self.mascotas = []
        self.veterinarios = []
            
        
    def registrarCliente(self):
        while True:
            try:
                id = len(self.clientes) + 1
                nombreCliente = input("Ingrese el nombre del cliente: ").strip()
                telefonoCliente = input("Ingrese el telefono del cliente: ").strip()
                direccionCliente = input("Ingrese el nombre del cliente: ").strip()
            
                if nombreCliente is None or telefonoCliente is None or direccionCliente is None:
                    raise ValueError("Todos los campos son obligatorios. Por favor intente de nuevo")

                cliente = Cliente(id, nombreCliente, telefonoCliente, direccionCliente)
                self.clientes.append(cliente)
                
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione <Enter> para continuar")
            
        