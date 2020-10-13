from PySimpleGUI import PySimpleGUI as sg
from random import randint
import back


class InicialPage:

    def __init__(self):
        sg.theme('SandyBeach')
        self.NAMES = back.read_task()
        self.exe()

    def front(self):
        flayout = [
            [sg.Text('Bem vindo(a)!')],
            [sg.Button('ENTRAR'), sg.Button('SAIR')]
        ]
        window1 = sg.Window('Tela Inicial', flayout, size=(500, 100), element_justification='center')
        button, values = window1.read()
        if button == 'ENTRAR':
            window1.close()
        if button in ('SAIR', None):
            exit()

    def funcionarios(self):
        layout = [
            [sg.Text('Digite o Nome do Funcionário: '), sg.Input(key='-NOME-', do_not_clear=False)],
            [sg.Button('Adicionar')],
            [sg.Text('')],
            [sg.Text('Funcionários cadastrados:')],
            [sg.Listbox(self.NAMES, size=(50, 10), key='-BOX-')],
            [sg.Button('Deletar'), sg.Button('Sair')]
        ]

        window = sg.Window('Funcionários', layout)

        while True:
            button, values = window.read()

            if button == 'Adicionar':
                ID = randint(1, 999)
                NAME = values['-NOME-'].capitalize()
                if NAME:
                    back.write(ID, NAME)
                self.NAMES = back.read_task()
                window.find_element('-BOX-').Update(self.NAMES)

            if button == 'Deletar':
                NAME = values['-BOX-'][0]
                if NAME:
                    back.delete(NAME)
                    self.NAMES = back.read_task()
                    window.find_element('-BOX-').Update(self.NAMES)

            if button in ('Sair', None):
                exit()

    def exe(self):
        self.front()
        self.funcionarios()


exe = InicialPage()

