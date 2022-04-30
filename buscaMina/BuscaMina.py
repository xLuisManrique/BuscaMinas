from tkinter import *
from celdas import Celda
import Ajustes
import Herramientas


raiz = Tk()

# Configuracion de la ventana del juego
raiz.configure(bg="black")
raiz.geometry(f"{Ajustes.width}x{Ajustes.height}")
raiz.title("Busca Mina")
raiz.resizable(False, False)

top_frame = Frame(
                raiz,
                bg="black",
                width=Ajustes.width,
                height=Herramientas.height_porcentaje(25)
)
top_frame.place(x=0, y=0)

titulo_juego = Label(
    top_frame,
    bg="black",
    fg="white",
    text="BuscaMinas",
    font=("", 36)
)
titulo_juego.place(
    x=Herramientas.width_porcentaje(40), y=0
)


left_frame = Frame(
                raiz,
                bg="black",
                width=Herramientas.width_porcentaje(25),
                height=Herramientas.height_porcentaje(75)
)
left_frame.place(x=0, y=Herramientas.height_porcentaje(25))

center_frame = Frame(
                    raiz,
                    bg="black",
                    width =Herramientas.width_porcentaje(75),
                    height=Herramientas.height_porcentaje(75),
)
center_frame.place(x=Herramientas.width_porcentaje(25), y=Herramientas.height_porcentaje(25))

for x in range(Ajustes.GRID_SIZE):
    for y in range(Ajustes.GRID_SIZE):
        c = Celda(x, y)
        c.crear_btn_object((center_frame))
        c.celda_btn_object.grid(column=y, row=x)

# Llamar a Label desde la clase Celda

Celda.crear_celda_contador_label(left_frame, None)

Celda.celda_contador_label_object.place(x=0 , y=0)

Celda.random_minas()



# Ejecutador de la ventana del juego
raiz.mainloop()