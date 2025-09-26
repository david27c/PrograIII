import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTK")
main.config(bg="#E4E2E2")
main.geometry("700x400")

style = ttk.Style(main)
style.theme_use("clam")

# ---- Función para cambiar el fondo ----
def cambiar_fondo():
    color_sel = radio_button1_var.get()
    if color_sel == 0:   # Salmón
        main.config(bg="salmon")
    elif color_sel == 1: # Celeste
        main.config(bg="skyblue")
    elif color_sel == 2: # Verde oscuro
        main.config(bg="darkgreen")

# ---- Frame para organizar ----
frame = ttk.Frame(main)
frame.pack(expand=True)

# ---- Radiobuttons ----
radio_button1_var = tk.IntVar(value=-1)  # -1 para que no haya selección inicial

style.configure("radio_button1.TRadiobutton", background="#ffffff", foreground="#000")
style.map("radio_button1.TRadiobutton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

radio_button1_0 = ttk.Radiobutton(frame, variable=radio_button1_var, text="Salmon", value=0, style="radio_button1.TRadiobutton")
radio_button1_0.pack(anchor="center", pady=5)

radio_button1_1 = ttk.Radiobutton(frame, variable=radio_button1_var, text="SkyBlue", value=1, style="radio_button1.TRadiobutton")
radio_button1_1.pack(anchor="center", pady=5)

radio_button1_2 = ttk.Radiobutton(frame, variable=radio_button1_var, text="DarkGreen", value=2, style="radio_button1.TRadiobutton")
radio_button1_2.pack(anchor="center", pady=5)

# ---- Botones ----
style.configure("button1.TButton", background="#E4E2E2", foreground="#000")
style.configure("button3.TButton", background="#E4E2E2", foreground="#000")

button1 = ttk.Button(frame, text="Cambiar", style="button1.TButton", command=cambiar_fondo)
button1.pack(pady=10)

button3 = ttk.Button(frame, text="Salir", style="button3.TButton", command=main.destroy)
button3.pack()

main.mainloop()
