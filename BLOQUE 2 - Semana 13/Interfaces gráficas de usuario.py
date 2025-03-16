#Creacion de una Aplicacion GUI Basica

import tkinter as tk
from tkinter import messagebox

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor GUI Jenny Cedeño")
        self.root.geometry("400x300")

        # Etiqueta y Campo de texto
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=5)

        # Botón Limpiar
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

    def add_data(self):
        data = self.entry.get()
        if data:
            self.listbox.insert(tk.END, data)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese un dato válido.")

    def clear_data(self):
        self.listbox.delete(0, tk.END)


# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
