import os

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_line(self):
        """Convierte el producto en una línea de texto para guardar en el archivo."""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"

    @staticmethod
    def from_line(line):
        """Crea un objeto Producto desde una línea de texto del archivo."""
        try:
            id_producto, nombre, cantidad, precio = line.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            print(f"Error al leer la línea del archivo: {line}")
            return None

# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()
        self.inicializar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de texto si existe."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as f:
                    for line in f:
                        producto = Producto.from_line(line)
                        if producto:
                            self.productos[producto.id_producto] = producto
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de texto."""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line())
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def inicializar_inventario(self):
        """Crea el inventario inicial si el archivo está vacío."""
        if not self.productos:  # Si no hay productos en el archivo, cargamos el inventario inicial
            print("Inicializando inventario con productos predeterminados...")
            productos_iniciales = [
                Producto("001", "Blusa", 5, 15.5),
                Producto("002", "Camisa", 20, 22.5),
                Producto("003", "Pantalón", 15, 35.0),
                Producto("004", "Zapatos Casuales", 10, 45.75),
                Producto("005", "Short", 20, 17.5),
                Producto("006", "Deportivos", 20, 60.0),
            ]
            for producto in productos_iniciales:
                self.productos[producto.id_producto] = producto
            self.guardar_inventario()

    def agregar_producto(self, producto):
        """Agrega un producto al inventario y lo guarda en el archivo."""
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe. Se actualiza la cantidad.")
            self.productos[producto.id_producto].cantidad += producto.cantidad
        else:
            self.productos[producto.id_producto] = producto

        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nombre, cantidad, precio):
        """Actualiza los datos de un producto."""
        if id_producto in self.productos:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, id_producto):
        """Busca un producto por su ID."""
        return self.productos.get(id_producto, "Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

# Función principal con menú de opciones
def main():
    inventario = Inventario()

    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            except ValueError:
                print("Error: Cantidad y precio deben ser valores numéricos.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nombre = input("Ingrese nuevo nombre: ")
            try:
                cantidad = int(input("Ingrese nueva cantidad: "))
                precio = float(input("Ingrese nuevo precio: "))
                inventario.actualizar_producto(id_producto, nombre, cantidad, precio)
            except ValueError:
                print("Error: Cantidad y precio deben ser valores numéricos.")

        elif opcion == "4":
            id_producto = input("Ingrese ID del producto a buscar: ")
            print(inventario.buscar_producto(id_producto))

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()