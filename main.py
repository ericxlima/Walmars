from PySimpleGUI import PySimpleGUI as sg


class InicialPage:

    def __init__(self):
        sg.theme('SandyBeach')
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
        if button == 'SAIR':
            exit()

    def funcionarios(self):
        layout = [
            [sg.Text('Digite o Nome do Funcionário: '), sg.Input(key='-NOME-')],
            [sg.Button('Adicionar')],
            [sg.Text('')],
            [sg.Text('Funcionários cadastrados:')],
            [sg.Listbox('NAMES', size=(50, 10), key='-BOX-')],
            [sg.Button('Deletar'), sg.Button('Sair')]
        ]

        window = sg.Window('Funcionários', layout)
        button, values = window.read()
        if button == 'Sair':
            exit()

    def exe(self):
        self.front()
        self.funcionarios()


exe = InicialPage()

