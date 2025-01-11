class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
class Cliente:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.identificador})"
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] += cantidad
        else:
            self.productos[producto.nombre] = {"producto": producto, "cantidad": cantidad}

    def eliminar_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]["cantidad"] -= cantidad
            if self.productos[producto.nombre]["cantidad"] <= 0:
                del self.productos[producto.nombre]
        else:
            print(f"El producto {producto.nombre} no está en el carrito.")

    def obtener_total(self):
        total = 0
        for item in self.productos.values():
            total += item["producto"].precio * item["cantidad"]
        return total

    def mostrar_detalles(self):
        print(f"Detalles del pedido del cliente {self.cliente.nombre} (ID: {self.cliente.identificador}):")
        for nombre, detalle in self.productos.items():
            producto = detalle["producto"]
            cantidad = detalle["cantidad"]
            print(f"  {producto}: {cantidad} unidades")
        print(f"Total: ${self.obtener_total()}")

# Crear productos
producto1 = Producto(nombre="Laptop", precio=1500)
producto2 = Producto(nombre="Smartphone", precio=1000)
producto3 = Producto(nombre="Auriculares", precio=150)

# Crear clientes
cliente1 = Cliente(identificador="C001", nombre="Virjilio Ajila")
cliente2 = Cliente(identificador="C002", nombre="Blanca Mero")

# Crear pedidos
pedido1 = Pedido(cliente1)
pedido2 = Pedido(cliente2)

# Agregar productos a los pedidos
pedido1.agregar_producto(producto1, cantidad=1)
pedido1.agregar_producto(producto2, cantidad=2)

pedido2.agregar_producto(producto3, cantidad=5)

# Mostrar detalles de los pedidos
pedido1.mostrar_detalles()
pedido2.mostrar_detalles()

# Eliminar productos de un pedido
pedido1.eliminar_producto(producto2, cantidad=1)

# Mostrar detalles después de eliminar
pedido1.mostrar_detalles()