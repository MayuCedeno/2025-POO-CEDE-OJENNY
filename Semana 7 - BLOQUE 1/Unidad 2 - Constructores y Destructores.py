# Ejemplo de la clase Estudiante que gestiona la creación y destrucción de un estudiante

class Estudiante:
    # Constructor __init__ que inicializa el nombre y la edad del estudiante
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Inicializa el atributo 'nombre'
        self.edad = edad      # Inicializa el atributo 'edad'
        print(f"Estudiante {self.nombre}, {self.edad} años, ha sido registrado.")

    # Destructor __del__ que simula la despedida del estudiante
    def __del__(self):
        print(f"Estudiante {self.nombre} se ha despedido.")

# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Jenny", 28)

# Eliminar el objeto estudiante1 explícitamente para simular que el estudiante se va
del estudiante1