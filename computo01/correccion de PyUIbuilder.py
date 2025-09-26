# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Controles TTK")
        self.ventana.geometry("400x300")  # Tamaño más compacto
        self.ventana.config(bg="#E4E2E2")

        self.valor = 0

        style = ttk.Style(self.ventana)
        style.theme_use("clam")

        # Estilo label
        style.configure("label1.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 24))

        # Label centrado
        self.label = ttk.Label(self.ventana, text=str(self.valor), style="label1.TLabel")
        self.label.pack(pady=20)

        # Botones
        self.boton_aumentar = ttk.Button(self.ventana, text="Aumentar", command=self.incrementar)
        self.boton_aumentar.pack(pady=10, ipadx=10, ipady=5)

        self.boton_disminuir = ttk.Button(self.ventana, text="Disminuir", command=self.decrementar)
        self.boton_disminuir.pack(pady=10, ipadx=10, ipady=5)

        self.boton_salir = ttk.Button(self.ventana, text="Salir", command=self.ventana.destroy)
        self.boton_salir.pack(pady=10, ipadx=10, ipady=5)

        self.ventana.mainloop()

    def incrementar(self):
        self.valor += 1
        self.label.config(text=self.valor)

    def decrementar(self):
        self.valor -= 1
        self.label.config(text=self.valor)


# Crear instancia
if __name__ == "__main__":
    app = Aplicacion()
