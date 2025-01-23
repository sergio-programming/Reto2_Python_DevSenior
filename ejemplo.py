class Persona:
    def __init__(self, id, nombre, telefono, edad):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.edad = edad
        

personas = []

def registrarPersonas():
    numeroDeClientes = int(input("Por favor el número de clientes que desea registrar: "))
    
    for i in range(numeroDeClientes):
        id = len(personas) + 1
        nombre = input("\nIngrese el nombre de la persona: ")
        telefono = input("Ingrese el telefono de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        
        persona = Persona(id, nombre, telefono, edad)
        personas.append(persona)
        
    print("\nCliente(s) registrado(s) exitosamente.")
    
def mostrarInformacion():
    personaEncontrada = None
    id = int(input("Ingrese el número del ID de la persona a encontrar: "))
    for persona in personas:
        if persona.id == id:
            personaEncontrada = persona
            break
    
    if personaEncontrada:
        return f"Id: {personaEncontrada.id} // Nombre: {personaEncontrada.nombre} // Telefono: {personaEncontrada.telefono} // Edad: {personaEncontrada.edad}"
    else:
        return "Persona no encontrada"
        
registrarPersonas()
print(mostrarInformacion())