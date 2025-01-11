# Este programa calcula el área de diferentes figuras geométricas
# (Círculo, Rectángulo, Triángulo) basándose en los datos proporcionados por el usuario.

import math  # Importamos la librería math para realizar cálculos matemáticos


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dada su radio"""
    return math.pi * radio ** 2  # Fórmula del área de un círculo: A = π * r²


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dada su base y altura"""
    return base * altura  # Fórmula del área de un rectángulo: A = base * altura


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y altura"""
    return 0.5 * base * altura  # Fórmula del área de un triángulo: A = 1/2 * base * altura


# Función principal para interactuar con el usuario y calcular el área
def calcular_area_figura():
    """Solicita al usuario los datos necesarios para calcular el área de una figura"""

    # Mostramos las opciones disponibles para el usuario
    print("Selecciona una figura para calcular su área:")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")

    # Solicitamos la opción del usuario
    seleccion = int(input("Ingresa el número de la figura (1-3): "))

    # Variable booleana para saber si la opción es válida
    es_opcion_valida = seleccion in [1, 2, 3]

    if not es_opcion_valida:
        print("Opción no válida. Por favor, elige una opción entre 1 y 3.")
        return

    # Dependiendo de la selección, pedimos los datos necesarios
    if seleccion == 1:  # Círculo
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es {area:.2f} unidades cuadradas.")

    elif seleccion == 2:  # Rectángulo
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo con base {base} y altura {altura} es {area:.2f} unidades cuadradas.")

    elif seleccion == 3:  # Triángulo
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo con base {base} y altura {altura} es {area:.2f} unidades cuadradas.")


# Llamamos a la función principal
calcular_area_figura()