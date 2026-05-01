import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                titular TEXT NOT NULL,
                saldo FLOAT NOT NULL,
                cpf TEXT NOT NULL UNIQUE
                 )""")


#  cursor.execute("""INSERT INTO  contas_bancarias
#               (titular, saldo, cpf) VALUES 
#                 ('mateus',  nome, saldo""")
 
cursor.execute("""SELECT  titular, saldo * FROM contas_bancarias""")
contas = cursor.fetchall()
for conta in contas:
    titular, saldo,  = conta
    print(f"""titular: {titular}
saldo:{saldo}""")
    print("\n")
conexao.commit()         # salva depois