import sqlite3 as sql

#  Criação e ativação da DataBase
banco = sql.connect('../database_records.db')
cursor = banco.cursor()

#  Tabela de Funcionários
cursor.execute('''CREATE TABLE IF NOT EXISTS employee_records(  id_employee INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                name TEXT NOT NULL UNIQUE,
                                                                password TEXT NOT NULL,
                                                                telephone VARCHAR(11),
                                                                sector VARCHAR(20) NOT NULL,
                                                                sex CHARACTER(1) )''')
banco.commit()


def write_employee(name, password, telephone, sector, sex):
    cursor.execute('''INSERT INTO employee_records(name, password, telephone, sector, sex) 
    VALUES(?, ?, ?, ?, ?)''', (name, password, telephone, sector, sex))
    banco.commit()


def delete_employee(name):
    cursor.execute('''DELETE FROM employee_records WHERE name = ?''', name)
    banco.commit()


def read_employees_names():
    cursor.execute('''SELECT NAME FROM employee_records''')
    data = cursor.fetchall()
    banco.commit()
    return data
