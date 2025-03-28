import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

# Función para agregar un evento a la lista

def agregar_evento():
    fecha = cal.get_date()  # Obtener la fecha seleccionada del calendario
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos")

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar el evento seleccionado?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la entrada de datos
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Calendario
cal = Calendar(frame_entrada, selectmode='day', date_pattern='dd/mm/yyyy')
cal.grid(row=0, column=0, padx=5, pady=5)

# Campo para ingresar la hora
lbl_hora = tk.Label(frame_entrada, text="Hora:")
lbl_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

# Campo para ingresar la descripción del evento
lbl_descripcion = tk.Label(frame_entrada, text="Descripción:")
lbl_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada, width=30)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Frame para mostrar la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# Tabla para visualizar los eventos almacenados
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.pack()

# Ejecutar la aplicación
root.mainloop()