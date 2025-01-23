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
        
class RegistroMascota(Mascota):
    def agregarAlHistorial(self, detallesServicio):
        self.historialCitas.append(detallesServicio)
        
    def obtenerHistorial(self):
        return self.historialCitas
    
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)          

class GestionVeterinaria:
    def __init__(self):
        self.clientes = []
        self.mascotas = []
        self.veterinarios = []
            
        
    def registrarCliente(self):
        while True:
            print("#"*30)
            print("MODULO DE REGISTRO DE CLIENTE")
            print("#"*30)
            try:
                id = len(self.clientes) + 1
                nombre = input("\nIngrese el nombre del cliente: ").strip()
                telefono = input("Ingrese el telefono del cliente: ").strip()
                direccion = input("Ingrese la d del cliente: ").strip()
            
                if nombre is None or telefono is None or direccion is None:
                    raise ValueError("\nTodos los campos son obligatorios. Por favor intente de nuevo")

                cliente = Cliente(id, nombre, telefono, direccion)
                self.clientes.append(cliente)
                print("Cliente registrado exitosamente")
                input("Presione <Enter> para continuar")
                break
                
            except ValueError as e:
                print(f"Error: {e}")
                input("Presione <Enter> para continuar")
            
    def actualizarCliente(self):
        cliente_a_modificar = None
        while True:
            print("#"*30)
            print("MODULO DE ACTUALIZACIÓN DE CLIENTE")
            print("#"*30)
            try:
                while True:
                    try:
                        id = int(input("\nIngrese el número de id del cliente: "))
                        for cliente in self.clientes:
                            if cliente.id == id:
                                cliente_a_modificar = cliente
                                break
                        
                        if cliente_a_modificar:
                            nuevoNombre = input("Ingrese el nombre del cliente: ").strip()
                            if nuevoNombre is None:
                                nuevoNombre = cliente_a_modificar._nombre
                                    
                            nuevoTelefono = input("Ingrese el telefono del cliente: ").strip()
                            if nuevoTelefono is None:
                                nuevoTelefono = cliente_a_modificar._telefono
                                    
                            nuevaDireccion = input("Ingrese la dirección del cliente: ").strip()
                            if nuevaDireccion is None:
                                nuevaDireccion = cliente_a_modificar._direccion
                                                              
                            
                            
                        else:
                            print("\nNo existe un cliente con el ID ingresado. Por favor intente de nuevo.")
                            input("Presione <Enter> para continuar")
                    except ValueError:
                        print("\nDebe ingresar un número valido. Por favor intente de nuevo.")
                        input("Presione <Enter> para continuar")
                        
                
                
            except print(0):
                pass