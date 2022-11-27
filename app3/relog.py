"""
    https://parzibyte.me/blog
"""
from datetime import datetime
import tkinter as tk
INTERVALO_REFRESCO_RELOJ = 1000  # En milisegundos


def obtener_hora_actual():
    h = datetime.now().strftime("%H:%M:%S")
    print(h)
    return h


def refrescar_reloj():
    print("Refrescando!")
    hora_actual = obtener_hora_actual()
    variable_hora_actual.set(hora_actual)
    print(variable_hora_actual)
    raiz.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value=obtener_hora_actual())
raiz.etiqueta = tk.Label(raiz, textvariable=variable_hora_actual, font=f"Consolas 150")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Reloj en Tkinter - By Parzibyte")
refrescar_reloj()
app.pack()
app.mainloop()