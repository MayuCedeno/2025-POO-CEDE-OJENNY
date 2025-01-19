# Clase base: Empleado
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.__salario = salario  # Atributo encapsulado


    def descripcion(self):
        return f"Empleado: {self.nombre}, Edad: {self.edad}, Salario: {self.__salario}"

    def get_salario(self):
        return self.__salario

# Metodo para cambiar el salario (encapsulación)
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("El salario debe ser un valor positivo")

 # Método para mostrar la acción del empleado
    def trabajar(self):
        return f"{self.nombre} está trabajando"


# Clase derivada: Gerente (heredada de Empleado)
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def descripcion(self):
        return (f"Gerente: {self.nombre}, Edad: {self.edad}, Salario: {self.get_salario()}, "
                f"Departamento: {self.departamento}")


# Clase derivada: Tecnico (hereda de Empleado)
class Tecnico(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def descripcion(self):
        return (f"Técnico: {self.nombre}, Edad: {self.edad}, Salario: {self.get_salario()}, "
                f"Especialidad: {self.especialidad}")


# Instancias y demostración
if __name__ == "__main__":
    # Crear un empleado genérico
    empleado = Empleado(nombre="Alan", edad=20, salario=3000)
    print(empleado.descripcion())

    # Crear un gerente
    gerente = Gerente(nombre="Adriana", edad=28, salario=6000, departamento="Ventas")
    print(gerente.descripcion())

    # Crear un técnico
    tecnico = Tecnico(nombre="Amy", edad=26, salario=3500, especialidad="Redes")
    print(tecnico.descripcion())

    # Mostrar encapsulación del salario
    print(f"Salario de {empleado.nombre}: {empleado.get_salario()}")
    empleado.set_salario(3200)
    print(f"Nuevo salario de {empleado.nombre}: {empleado.get_salario()}")