import sqlite3 as sql


class DataBase:
    def __init__(self):
        self.banco = sql.connect('card.s3db')
        self.cursor = self.banco.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY AUTOINCREMENT,
                        number TEXT,
                        pin TEXT,
                        balance INTEGER DEFAULT 0)''')

    def insert_into_table(self, values):
        self.cursor.execute('INSERT INTO card(number, pin, balance) VALUES(?, ?, ?)', values)
        self.banco.commit()

    def load_cards(self):
        self.cursor.execute('SELECT * FROM card')
        data = self.cursor.fetchall()
        self.banco.commit()
        return data

    def delete_account(self, number):
        self.cursor.execute('DELETE FROM card WHERE number = ?', (number,))
        self.banco.commit()

    def add_balance(self, money, card):
        self.cursor.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (money, card))
        self.banco.commit()

    def transference(self, money, card1, card2):
        self.cursor.execute('UPDATE card SET balance = balance - ? WHERE number = ?', (money, card1))
        self.cursor.execute('UPDATE card SET balance = balance + ? WHERE number = ?', (money, card2))
        self.banco.commit()