import sys
from tkinter import Button, Label
import random
import Ajustes
import ctypes
import sys



class Celda:
    all = []
    celda_contador = Ajustes.CELL_CONTADOR
    celda_contador_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.celda_btn_object = None
        self.x = x
        self.y = y

        # Añadir el objeto a la lista Celda.all
        Celda.all.append(self)

    def crear_btn_object(self, ubicacion):
        boton = Button(
            ubicacion,
            width=12,
            height=4,
        )
        boton.bind('<Button-1>', self.click_derecho_actions)  # Left Click
        boton.bind('<Button-3>', self.click_izquiero_actions)  # Right Click
        self.celda_btn_object = boton


    @staticmethod
    def crear_celda_contador_label(self, ubicacion):
        lbl = Label(
            ubicacion,
            bg="black",
            fg="white",

            text=f"Celda Izquierda: {Celda.celda_contador}",
            font=("", 16)
        )
        Celda.celda_contador_label_object = lbl
    

    def click_derecho_actions(self, evento):
        if self.is_mine:
            self.mina_escondida()
        else:
            if self.surrounded_cells_mines_length == 0:
                for celda_obj in self.surrounded_cells:
                    celda_obj.mostrar_celda()
            self.mostrar_celda()

            # Jugador Gana
            if Celda.celda_contador == Ajustes.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "Ganaste!", "Juego terminado", 0)


    # Cancelar Click Derecho - Izquierdo si celda ya se ha clickeado:
        self.celda_btn_object.unbind('<Button-1>')
        self.celda_btn_object.unbind('<Button-3>')


    def get_celda_by_axis(self, x, y):
        # Retornar un objeto de la celda basado en los valores de x, y
        for celda in Celda.all:
            if celda.x == x and celda.y == y:
                return celda

    @property
    def surrounded_cells(self):
        cells = [
            self.get_celda_by_axis(self.x - 1, self.y - 1),
            self.get_celda_by_axis(self.x - 1, self.y),
            self.get_celda_by_axis(self.x - 1, self.y + 1),
            self.get_celda_by_axis(self.x, self.y - 1),
            self.get_celda_by_axis(self.x + 1, self.y - 1),
            self.get_celda_by_axis(self.x + 1, self.y),
            self.get_celda_by_axis(self.x + 1, self.y + 1),
            self.get_celda_by_axis(self.x, self.y + 1)
        ]

        cells = [celda for celda in cells if celda is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        contador = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                contador += 1
        return contador



    def mostrar_celda(self):
        if not self.is_opened:
            Celda.celda_contador -= 1
            self.celda_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Reemplazar el texto del contador de celda label con un nuevo contador
            if Celda.celda_contador_label_object:
                Celda.celda_contador_label_object.configure(
                    text=f"Celda izquierda: {Celda.celda_contador}"
                )
            # Cambiar el color de fondo en caso tal que sea un candidato a mina(color amarillo)
            self.celda_btn_object.configure(
                bg="SystemButtonFace"
            )
        # Mark the cell as opend( Use is as the last line of this method)
        self.is_opened = True


    def mina_escondida(self):
        self.celda_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, "Diste con una mina", "GAME OVER PAPU", 0)
        sys.exit()




    def click_izquiero_actions(self, evento):
        if not self.is_mine_candidate:
            self.celda_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.celda_btn_object.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_candidate = False


    @staticmethod
    def random_minas():
        picked_celdas = random.sample(
            Celda.all, int(Ajustes.MINES_COUNT)
        )
        for picked_celdas in picked_celdas:
            picked_celdas.is_mine = True

    def __repr__(self):
        return f"Celda({self.x}, {self.y}"
