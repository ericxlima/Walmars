from database_management import DataBase
from PySimpleGUI import PySimpleGUI as sg
from random import randint


class CardManagement:

    @staticmethod
    def luhn_implementacion(number_to_check=None):
        if not number_to_check:
            is_valid = False
            number = ''
            while not is_valid:
                number_list = list(map(int, list('400000' + '{:0<10}'.format(randint(0, 9999999999).__str__()))))
                new_card_list = []
                for k, v in enumerate(number_list):
                    if k % 2 == 0:
                        new_card_list.append(v * 2 if v * 2 <= 9 else v * 2 - 9)
                    else:
                        new_card_list.append(v)
                if sum(new_card_list) % 10 == 0:
                    number = ''.join(map(str, number_list))
                    is_valid = True
            return number
        else:
            new_card_list = []
            for k, v in enumerate(list(map(int, list(number_to_check)))):
                if k % 2 == 0:
                    new_card_list.append(v * 2 if v * 2 <= 9 else v * 2 - 9)
                else:
                    new_card_list.append(v)
            if sum(new_card_list) % 10 == 0:
                return True

    def __init__(self):
        self.__banco = DataBase()
        sg.theme('SandyBeach')
        self.__front_page()

    def __front_page(self):
        front_layout = [
            [sg.Text('Bem vindo(a)!')],
            [sg.Button('CRIAR CONTA'), sg.Button('LOGAR CONTA'), sg.Button('SAIR')]
        ]
        window = sg.Window('Página Inicial', front_layout, size=(500, 100), element_justification='center')
        button, values = window.read(close=True)
        if button == 'CRIAR CONTA':
            self.__criar_conta()
        if button == 'LOGAR CONTA':
            self.__logar_conta()
        if button in ('SAIR', None):
            exit()

    def __criar_conta(self):
        self.__data = self.__banco.load_cards()
        new_card_number = self.luhn_implementacion()
        if new_card_number not in [data[1] for data in self.__data]:
            card_pin = '{:0<4}'.format(randint(0, 9999).__str__())
            self.__banco.insert_into_table((new_card_number, card_pin, 0))
            pop_up_layout = [
                [sg.Text('Seu cartão foi criado com êxito')],
                [sg.Text('Seu número de cartão:'),
                 sg.Input(default_text=new_card_number, disabled=True, size=(16, 1))],
                [sg.Text('Sua senha:'),
                 sg.Input(default_text=card_pin, disabled=True, size=(4, 1))]
            ]
            pop_up_window = sg.Window('Criação de Cartão', pop_up_layout, element_justification='center')
            pop_up_window.read(close=True)
            self.__front_page()

    def __logar_conta(self):
        self.__data = self.__banco.load_cards()
        log_layout = [
            [sg.Text('Insira o número do cartão:'), sg.Input(key='-NUMERO-')],
            [sg.Text('Insira a senha do cartão:'), sg.Input(key='-SENHA-')],
            [sg.Submit('Enviar'), sg.Cancel('Voltar')]
        ]
        log_window = sg.Window('Login no Sistema', log_layout, element_justification='center')
        button, values = log_window.read(close=True)
        if button == 'Enviar':
            if [x for x in self.__data if values['-NUMERO-'] in x and values['-SENHA-'] in x]:
                sg.popup('Você conseguiu logar na sua conta com sucesso!', title='Sucesso')
                self.__administrar_conta(values['-NUMERO-'])
            else:
                sg.popup('Ocorreu um erro ao processar as informações', title='Erro')
                self.__front_page()
        else:
            self.__front_page()

    def __transferencia(self, number):
        deposito_layout = [
            [sg.Text('Insira o número do destinatário:'), sg.Input(key='-NUMERO-')],
            [sg.Text('Insira o valor a ser depositado:'), sg.Input(key='-VALOR-')],
            [sg.Submit('ENVIAR'), sg.Cancel('VOLTAR')]
        ]
        deposito_window = sg.Window('Depósito', deposito_layout, element_justification='center')
        while True:
            button, values = deposito_window.read(close=True)
            if button == 'ENVIAR':
                if values['-NUMERO-'] == number:
                    sg.popup()
                self.__banco.transference(values['-VALOR-'], number, values['-NUMERO-'])

    def __administrar_conta(self, numero):





        self.__data = {x[1]: x[-1] for x in self.__data}
        logado_layout = [
            [sg.Text('Escolha uma opção: ')],
            [sg.B('SALDO'), sg.B('DEPÓSITO'), sg.B('TRANSFERIR'), sg.B('FECHAR CONTA'), sg.B('SAIR')]
        ]
        logado_window = sg.Window('Administrar conta', logado_layout, element_justification='center')
        while True:
            button, values = logado_window.read(close=True)
            if button == 'SALDO':
                sg.popup('Seu saldo é de {}'.format(self.__data[numero]), title='Saldo')
            if button == 'DEPÓSITO':
                value = sg.popup_get_text('Insira o quanto você quer depositar:', title='Depósito')
                self.__banco.add_balance(value, numero)
            if button in (None, 'SAIR'):
                self.__front_page()




def luhn_implementacion(s):
    return s


def login(user_number, banco):
    choice2 = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')
    while choice2 != '5':
        if choice2 == '1':
            print([x[-1] for x in banco.load_cards() if user_number in x][0])
        if choice2 == '2':
            income = int(input('\nEnter income:\n'))
            banco.update_balance(income, user_number)
            print('Income was added!')

        if choice2 == '3':
            transfer_card = input('\nTransfer\nEnter card number:\n')
            cards = {x[1]: x[-1] for x in banco.load_cards()}
            if not luhn_implementacion(transfer_card):
                print('Probably you made a mistake in the card number. Please try again!\n')
            elif transfer_card not in cards.keys():
                print('Such a card does not exist.\n')
            else:
                transfer_money = int(input('\nEnter how much money you want to transfer:\n'))
                if transfer_money > int(cards[user_number]):
                    print('Not enough money!')
                else:
                    banco.transference(transfer_money, user_number, transfer_card)
                    print('Success')

        if choice2 == '4':
            banco.delete_account(user_number)

        if choice2 == '0':
            return True  # para encerrar o programa futuramente
        choice2 = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')


test = CardManagement()
