import os
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana 2 - BLOQUE 1/Semana 2 - Desarrollo de Ejemplos de Técnicas de Programación (POO).py',
        '2': 'Semana 3 - BLOQUE 1/Semana 3 - Comparación de Programación Tradicional y POO en Python.py',
        '3': 'Semana 4 - BLOQUE 1/EjemplosMundoReal_POO.py',
        '4': 'Semana 5 - BLOQUE 1/tipos de datos, identificadores y convenciones de nomenclatura en Python.Py',
        '5': 'Semana 6 - BLOQUE 1/Unidad 2 - Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '6': 'Semana 7 - BLOQUE 1/Unidad 2 - Constructores y Destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }
    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()