from tkinter import Tk, ttk, Frame, PhotoImage
from tkinter import Button, Entry, Label, Menu, Scrollbar, Text
from tkinter import messagebox, filedialog, Toplevel, colorchooser
from tkinter import font, BooleanVar

import self as self


class ventana(Frame):
    def __init__(self):
        super(ventana,self).__init__()
    self.master.tittle('Bloc de Notas')
    self.master.iconbitmap('icono.ico')
    self.master.geometry('700*500+380+20')
    self.master.protocol("WM_DELETE_WINDOW", self.salir)

    self.señal_ajuste = BooleanVar()
    self.info_estado = BooleanVar()
    self.info_estado.set(False)
    self.señal_ajustes.set(True)
    self.clik_aceptar = False
    self.x = 0
    self.y = 0
    self.n = 12
    self.f = 'Arial'

    def salir(self):
        valor = messagebox.askyesno('salir', '¿Desea salir?', parent=self.master)
        if valor == True:
            self.master.destroy()
            self.master.quit()

    if __name__ = "__main__":
        ventana = Tk()
        app = ventana = Tk(ventana)
        app.mainloop()
