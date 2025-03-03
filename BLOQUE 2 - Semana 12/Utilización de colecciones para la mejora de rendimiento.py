import json


class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }


class Usuario:
    def __init__(self, id_usuario, nombre, libros_prestados=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = libros_prestados if libros_prestados is not None else []

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "libros_prestados": self.libros_prestados
        }


class Biblioteca:
    def __init__(self, archivo_libros='libros.json', archivo_usuarios='usuarios.json'):
        self.archivo_libros = archivo_libros  # Corregido
        self.archivo_usuarios = archivo_usuarios
        self.libros = self.cargar_datos(self.archivo_libros)
        self.usuarios = self.cargar_datos(self.archivo_usuarios)

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_datos(self, archivo, datos):
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro.to_dict()
        self.guardar_datos(self.archivo_libros, self.libros)
        print(f"Libro '{libro.titulo}' añadido correctamente.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario.to_dict()
        self.guardar_datos(self.archivo_usuarios, self.usuarios)
        print(f"Usuario '{usuario.nombre}' registrado correctamente.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros and not self.libros[isbn]['prestado']:
            self.libros[isbn]['prestado'] = True  # Corregido
            self.usuarios[id_usuario]['libros_prestados'].append(isbn)
            self.guardar_datos(self.archivo_libros, self.libros)
            self.guardar_datos(self.archivo_usuarios, self.usuarios)
            print(f"Libro '{isbn}' prestado a usuario '{id_usuario}'.")
        else:
            print("No se puede prestar el libro. Verifique si el usuario existe o si el libro ya está prestado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.usuarios[id_usuario]["libros_prestados"]:
            self.usuarios[id_usuario]["libros_prestados"].remove(isbn)
            self.libros[isbn]["prestado"] = False
            self.guardar_datos(self.archivo_libros, self.libros)
            self.guardar_datos(self.archivo_usuarios, self.usuarios)
            print(f"Libro '{isbn}' devuelto por usuario '{id_usuario}'.")
        else:
            print("No se puede devolver el libro. Verifique si el usuario y el libro existen en el registro.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self.libros.values():
                estado = "Prestado" if libro['prestado'] else "Disponible"
                print(f"ISBN: {libro['isbn']} | {libro['titulo']} - {libro['autor']} ({libro['categoria']}) - {estado}")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            for usuario in self.usuarios.values():
                print(
                    f"Usuario ID: {usuario['id_usuario']} | Nombre: {usuario['nombre']} | Libros Prestados: {usuario['libros_prestados']}")


def menu():
    biblioteca = Biblioteca()
    while True:
        print("\nMenú de Biblioteca")
        print("1. Añadir Libro")
        print("2. Registrar Usuario")
        print("3. Mostrar Libros")
        print("4. Prestar Libro")
        print("5. Devolver Libro")
        print("6. Mostrar Usuarios")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)

        elif opcion == '2':
            id_usuario = input("ID Usuario: ")
            nombre = input("Nombre: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '3':
            biblioteca.mostrar_libros()

        elif opcion == '4':
            id_usuario = input("ID Usuario: ")
            isbn = input("Código del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '5':
            id_usuario = input("ID Usuario: ")
            isbn = input("Código del libro: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '6':
            biblioteca.mostrar_usuarios()

        elif opcion == '7':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()