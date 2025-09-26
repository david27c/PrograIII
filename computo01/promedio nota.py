import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Promedio de Cómputo 01")
        self.ventana1.geometry('400x300')

        # Lab 1
        self.label1 = tk.Label(self.ventana1, text="Nota Lab 1 (30%):")
        self.label1.grid(column=0, row=0, padx=10, pady=5, sticky="e")
        self.lab1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.lab1)
        self.entry1.grid(column=1, row=0, padx=10, pady=5)

        # Lab 2
        self.label2 = tk.Label(self.ventana1, text="Nota Lab 2 (30%):")
        self.label2.grid(column=0, row=1, padx=10, pady=5, sticky="e")
        self.lab2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.lab2)
        self.entry2.grid(column=1, row=1, padx=10, pady=5)

        # Parcial
        self.label3 = tk.Label(self.ventana1, text="Nota Parcial (40%):")
        self.label3.grid(column=0, row=2, padx=10, pady=5, sticky="e")
        self.parcial = tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, width=10, textvariable=self.parcial)
        self.entry3.grid(column=1, row=2, padx=10, pady=5)

        # Botón
        self.boton1 = tk.Button(self.ventana1, text="Calcular Promedio", command=self.calcular)
        self.boton1.grid(column=0, row=3, columnspan=2, pady=15)

        # Resultado
        self.label_resultado = tk.Label(self.ventana1, text="El promedio aparecerá aquí", font=("Arial", 12))
        self.label_resultado.grid(column=0, row=4, columnspan=2, pady=10)

        self.ventana1.mainloop()

    def calcular(self):
        try:
            # Obtener valores
            nota_lab1 = float(self.lab1.get())
            nota_lab2 = float(self.lab2.get())
            nota_parcial = float(self.parcial.get())

            # Calcular promedio con ponderación
            promedio = (nota_lab1 * 0.30) + (nota_lab2 * 0.30) + (nota_parcial * 0.40)

            # Mostrar resultado
            self.label_resultado.configure(
                text=f"Tu promedio es: {nota_lab2:.2f}"
            )
        except:
            self.label_resultado.configure(text="⚠️ Ingresa notas válidas.")

aplicacion1 = Aplicacion()
