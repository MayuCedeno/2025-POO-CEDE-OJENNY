# Programación Tradicional
# Cálculo del promedio semanal del clima

def ingresar_temperaturas():
    """Función para ingresar las temperaturas diarias."""
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Función para calcular el promedio de las temperaturas."""
    return sum(temperaturas) / len(temperaturas)

# Uso de las funciones en la programación tradicional
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Programación Orientada a Objetos (POO)
class ClimaSemanal:
    def __init__(self):
        """Inicializa una lista para las temperaturas."""
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias."""
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio de las temperaturas."""
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase ClimaSemanal
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()
print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")
