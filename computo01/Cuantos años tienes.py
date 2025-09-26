import tkinter as tk
from datetime import date

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora de Edad")
        self.ventana1.geometry('450x300')

        # Año de nacimiento
        self.label1 = tk.Label(self.ventana1, text="Año de nacimiento:")
        self.label1.grid(column=0, row=0, padx=10, pady=5, sticky="e")
        self.anio_nac = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.anio_nac)
        self.entry1.grid(column=1, row=0, padx=10, pady=5)

        # Mes de nacimiento
        self.label2 = tk.Label(self.ventana1, text="Mes de nacimiento (1-12):")
        self.label2.grid(column=0, row=1, padx=10, pady=5, sticky="e")
        self.mes_nac = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.mes_nac)
        self.entry2.grid(column=1, row=1, padx=10, pady=5)

        # Día de nacimiento
        self.label3 = tk.Label(self.ventana1, text="Día de nacimiento:")
        self.label3.grid(column=0, row=2, padx=10, pady=5, sticky="e")
        self.dia_nac = tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, width=10, textvariable=self.dia_nac)
        self.entry3.grid(column=1, row=2, padx=10, pady=5)

        # Año actual
        self.label4 = tk.Label(self.ventana1, text="Año actual:")
        self.label4.grid(column=0, row=3, padx=10, pady=5, sticky="e")
        self.anio_act = tk.StringVar()
        self.entry4 = tk.Entry(self.ventana1, width=10, textvariable=self.anio_act)
        self.entry4.grid(column=1, row=3, padx=10, pady=5)

        # Botón
        self.boton1 = tk.Button(self.ventana1, text="Calcular Edad", command=self.calcular)
        self.boton1.grid(column=0, row=4, columnspan=2, pady=15)

        # Resultado
        self.label_resultado = tk.Label(self.ventana1, text="Tu edad aparecerá aquí", font=("Arial", 12))
        self.label_resultado.grid(column=0, row=5, columnspan=2, pady=10)

        self.ventana1.mainloop()

    def calcular(self):
        try:
            # Datos ingresados
            anio_nac = int(self.anio_nac.get())
            mes_nac = int(self.mes_nac.get())
            dia_nac = int(self.dia_nac.get())
            anio_act = int(self.anio_act.get())

            # Fecha de nacimiento y fecha actual
            nacimiento = date(anio_nac, mes_nac, dia_nac)
            hoy = date(anio_act, date.today().month, date.today().day)

            # Calcular edad
            edad_anios = hoy.year - nacimiento.year
            edad_meses = hoy.month - nacimiento.month
            edad_dias = hoy.day - nacimiento.day

            # Ajustes cuando el mes/día no ha llegado aún
            if edad_dias < 0:
                edad_meses -= 1
                # Corregimos días tomando prestado del mes anterior
                dias_mes_anterior = (date(hoy.year, hoy.month, 1) - date(hoy.year, hoy.month - 1, 1)).days
                edad_dias += dias_mes_anterior

            if edad_meses < 0:
                edad_anios -= 1
                edad_meses += 12

            # Mostrar resultado
            self.label_resultado.configure(
                text=f"Tienes {edad_anios} años, {edad_meses} meses y {edad_dias} días."
            )

        except Exception as e:
            self.label_resultado.configure(text="⚠️ Datos inválidos, inténtalo de nuevo.")

aplicacion1 = Aplicacion()
