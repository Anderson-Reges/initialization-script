from tkinter import (
    Tk, Frame,
    Label, Button,
)


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.containerPrincipal = Frame(master, borderwidth=2, relief="groove")
        self.containerPrincipal.config(width=500, height=400)
        self.containerPrincipal.pack(expand=True)

        self.titulo = Label(self.containerPrincipal, text="Escolha a Opção:")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.initialization = Button(self.containerPrincipal)
        self.initialization["text"] = "Iniciar Programas"
        self.initialization["font"] = ("Calibri", "8")
        self.initialization["width"] = 12
        self.initialization.pack(side="left")

        self.choose_programs = Button(self.containerPrincipal)
        self.choose_programs["text"] = "Escolha programas para iniciar"
        self.choose_programs["font"] = ("Calibri", "8")
        self.choose_programs["width"] = 22
        self.choose_programs.pack(side="right")


root = Tk()
Application(root)
root.mainloop()
