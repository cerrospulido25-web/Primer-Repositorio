#Diana Cerros Pulido
#CBTIS 89
#3 B programacion

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("300x200")

# Etiqueta de texto
etiqueta = tk.Label(ventana, text="NOMBRE Y APELLIDO:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Cuadro de texto
entrada1= tk.Entry(ventana, font=("Arial", 12))
entrada1.pack(pady=5)

# Cuadro de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=4)

# Botón que responde a un evento
def mostrar_texto():
    texto1 = entrada1.get()
    texto2 = entrada. get ()
    etiqueta_resultado.config(text=f"Escribiste: {texto1} {texto2}")

boton = tk.Button(ventana, text="Mostrar Nombre", command=mostrar_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=5)

# Iniciar el loop principal
ventana.mainloop()