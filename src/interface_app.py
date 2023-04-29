from tkinter import (
    Tk,
    Frame,
    Label,
    Button,
    Checkbutton,
    Entry,
)
from config_apps import Config


class Application:
    def __init__(self, master=None):
        self.config = Config("Apps.pickle")
        self.config.load()
        print(self.config.apps)
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
        self.choose_programs["command"] = self.set_app
        self.choose_programs.pack(side="right")

    def set_app(self):
        self.containerAddApp = Frame(root, borderwidth=2, relief="groove")
        self.containerAddApp.config(width=500, height=400)
        self.containerAddApp.pack(expand=True)

        self.containerPrincipal2 = Frame(root, borderwidth=2, relief="groove")
        self.containerPrincipal2.pack(expand=True)

        self.titulo2 = Label(
            self.containerPrincipal2, text="Lista de Programas:"
            )
        self.titulo2["font"] = ("Arial", "10", "bold")
        self.titulo2.pack()

        self.program2 = Checkbutton(
            self.containerPrincipal2, text="Programa 2"
        )
        self.program2["font"] = ("Calibri", "8")
        self.program2.pack()

        self.back_button = Button(self.containerPrincipal2)
        self.back_button["text"] = "Voltar para a primeira interface"
        self.back_button["font"] = ("Calibri", "8")
        self.back_button["width"] = 30
        self.back_button["command"] = self.hide_second_interface
        self.back_button.pack(side="bottom")

        self.title_add = Label(
            self.containerAddApp, text="Adicione um programa:"
        )
        self.title_add.pack()

        self.input = Entry(self.containerAddApp)
        self.input["width"] = 30
        self.input["font"] = self.fontePadrao
        self.input.pack(side="left")

        self.add_app_button = Button(self.containerAddApp)
        self.add_app_button["text"] = "Salvar app"
        self.add_app_button["font"] = ("Calibri", "8")
        self.add_app_button["width"] = 30
        self.add_app_button["command"] = self.save_app
        self.add_app_button.pack(side="bottom")

        self.containerPrincipal.pack_forget()

    def hide_second_interface(self):
        self.containerPrincipal2.destroy()
        self.containerAddApp.destroy()
        self.containerPrincipal.pack()

    def save_app(self):
        app = self.input.get()
        self.config.add_app(app)
        self.config._save()


root = Tk()
Application(root)
root.mainloop()
