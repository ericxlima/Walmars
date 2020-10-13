from PySimpleGUI import PySimpleGUI as sg
from database_management import back


class InicialPage:

    def __init__(self):
        sg.theme('SandyBeach')
        self.names = back.read_employees_names()
        self.exe()

    def front(self):
        flayout = [
            [sg.Text('Bem vindo(a)!')],
            [sg.Button('FUNCIONÁRIOS'), sg.Button('SAIR', size=(6, 0))]
        ]
        window = sg.Window('Tela Inicial', flayout, size=(500, 100), element_justification='center')
        button, values = window.read()
        if button == 'FUNCIONÁRIOS':
            window.close()
        if button in ('SAIR', None):
            exit()

    def funcionarios(self):
        layout = [
            [sg.Text('Digite o Nome do Funcionário:  '), sg.In(key='-NOME-', do_not_clear=False)],
            [sg.Text('Digite a Senha do Funcionário: '), sg.In(key='-SENHA-', do_not_clear=False, password_char='*')],
            [sg.Text('Insira o número de Telefone:   '), sg.In(key='-TEL-', do_not_clear=False, size=(11, 0))],
            [sg.T('Escolha o setor: '), sg.Combo(['Administração', 'Telemarketing', 'Marketing',
                                                  'Gerência', 'Vendas', 'Serviços'], key='-SETOR-', size=(15, 0))],
            [sg.T('Sexo:', size=(17, 0)), sg.Rad('Masculino', 'sex', k='-MASC-'), sg.Rad('Feminino', 'sex', k='-FEM-'),
             sg.Rad('Não Informar', 'sex', k='-NOSEX-', default=True)],
            [sg.Button('Cadastrar')],
            [sg.Text('')],
            [sg.Text('Funcionários cadastrados:')],
            [sg.Listbox(self.names, size=(50, 10), key='-BOX-')],
            [sg.Button('Deletar'), sg.Button('Sair')]
        ]

        window = sg.Window('Funcionários', layout)

        while True:
            button, values = window.read()

            if button == 'Cadastrar':
                v = values
                if not v['-NOME-'].isalpha():
                    sg.popup('Insira um Nome válido')
                elif not v['-SENHA-']:
                    sg.popup('Insira uma Senha válida')
                elif not v['-SETOR-']:
                    sg.popup('É obrigatório selecionar o Setor')
                else:
                    dados = (v['-NOME-'].capitalize(), v['-SENHA-'], v['-TEL-'], v['-SETOR-'])
                    sex = '-'
                    if v['-MASC-']:
                        sex = 'M'
                    elif v['-FEM-']:
                        sex = 'F'
                    dados = dados + tuple(sex)
                    print(dados)
                    back.write_employee(*dados)
                    self.names = back.read_employees_names()
                    window.find_element('-BOX-').Update(self.names)

            if button == 'Deletar':
                nome = values['-BOX-'][0]
                if nome:
                    back.delete_employee(nome)
                    self.names = back.read_employees_names()
                    window.find_element('-BOX-').Update(self.names)

            if button in ('Sair', None):
                exit()

    def exe(self):
        self.front()
        self.funcionarios()


exe = InicialPage()
