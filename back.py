import sqlite3 as sql


#  Criação e ativação da DataBase

banco = sql.connect('employee_records.db')
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employee_records(
                        ID INT PRIMARY KEY NOT NULL,
                        NAME TEXT NOT NULL)''')

#  Aplicando mudanças na Database
banco.commit()


def write(ID, NAME):
    cursor.execute('''INSERT INTO employee_records(ID, NAME) VALUES(?, ?)''', (ID, NAME))
    banco.commit()

def delete(NAME):
    cursor.execute('''DELETE FROM employee_records WHERE NAME = ?''', NAME)
    banco.commit()

def read_task():
    cursor.execute('''SELECT NAME FROM employee_records''')
    data = cursor.fetchall()
    banco.commit()
    return data
