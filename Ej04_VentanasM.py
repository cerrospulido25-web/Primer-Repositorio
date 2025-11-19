#Diana Cerros Pulido
#CBTIS 89
#3 B programacion

import tkinter as tk
from tkinter import Toplevel

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

# Función para abrir una Nombre Apellido
def Nombre_Apellido():
    Nombre_Apellido = Toplevel(ventana_principal)
    Nombre_Apellido.title("Nombre y Apellido")
    Nombre_Apellido.geometry("250x150")
    
    etiqueta = tk.Label(Nombre_Apellido, text="Diana Cerros", font=("Arial", 12))
    etiqueta.pack(pady=10)

    boton_cerrar = tk.Button(Nombre_Apellido, text="Cerrar", command=Nombre_Apellido.destroy)
    boton_cerrar.pack(pady=10)

    # Función para abrir una Programando con python
def Programando_con_python2():
    programando_con_python2= Toplevel(ventana_principal)
    programando_con_python2.title("programando con python")
    programando_con_python2.geometry("250x150")
    
    etiqueta2 = tk.Label(programando_con_python2, text="Programando con python", font=("Arial", 12))
    etiqueta2.pack(pady=10)

    boton_cerrar2 = tk.Button(programando_con_python2, text="Cerrar", command=programando_con_python2.destroy)
    boton_cerrar2.pack(pady=10)

 
# Botón en la ventana principal para   Nombre Apellido
boton_abrir = tk.Button(ventana_principal, text=" Nombre Apellido", command=Nombre_Apellido)
boton_abrir.pack(pady=20)


# Botón en la ventana principal para   Nombre Apellido
boton_abrir = tk.Button(ventana_principal, text="programando con python", command=Programando_con_python2)
boton_abrir.pack(pady=20)


# Iniciar el loop principal
ventana_principal.mainloop()


