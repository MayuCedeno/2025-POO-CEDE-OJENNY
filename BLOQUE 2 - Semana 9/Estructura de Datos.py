# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor para inicializar los atributos de la clase
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Método que devuelve una representación del producto para mostrarlo fácilmente
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        # Inicialización de la lista de productos como un diccionario vacío
        self.productos = {}

    def agregar_producto(self, producto):
        # Método para agregar un nuevo producto, asegurando que el ID sea único
        if producto.id_producto in self.productos:
            print("Error: Producto con este ID ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print(f"Producto '{producto.nombre}' agregado con éxito.")

    def eliminar_producto(self, id_producto):
        # Método para eliminar un producto por su ID
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Método para actualizar la cantidad y/o precio de un producto por su ID
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado con éxito.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Método para buscar productos por nombre, permite coincidencias parciales
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        # Método para mostrar todos los productos en el inventario
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

# Función para mostrar el menú e interactuar con el usuario
def menu():
    inventario = Inventario()  # Creamos una instancia de la clase Inventario

    # Agregar productos predeterminados
    inventario.agregar_producto(Producto("001", "Blusa", 5, 15.5))
    inventario.agregar_producto(Producto("002", "Camisa", 20, 22.5))
    inventario.agregar_producto(Producto("003", "Pantalón", 15, 35.0))
    inventario.agregar_producto(Producto("004", "Zapatos Casuales", 10, 45.75))
    inventario.agregar_producto(Producto("005", "Short", 20, 17.5))
    inventario.agregar_producto(Producto("006", "Deportivos", 20, 60.0))

    while True:
        # Mostramos el menú de opciones
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break  # Salir del programa

        elif opcion == '1':
            # Agregar producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            # Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            # Mostrar inventario
            inventario.mostrar_inventario()

        else:
            print("Opción inválida, intente nuevamente.")

# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    menu()