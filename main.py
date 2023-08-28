import pyodbc
import pandas as pd

# Insere dados da conexão com o banco de dados
data_con = (
    "Driver={SQL Server};"
    "Server=DESKTOP-Q6OMQ27;"
    "Database=python_sql;"
)

# Abre a conexão com o banco de dados passando como parametro os dados da conexão
con = pyodbc.connect(data_con)
if con:
    print('Conectado ao banco de dados!')
else:
    print('Algo deu errado com a conexão!')

cursor = con.cursor()


while True:

    nome = input('Digite o nome: ')
    email = input('Digite o Email: ')
    data_nascimento = input('Digite a data de nascimento (dd/mm/aaaa): ')

    cmd_insert = f""" INSERT INTO Usuarios(Nome, Email, DataNascimento)
            VALUES ('{nome}', '{email}', '{data_nascimento}'); """
    
    cursor.execute(cmd_insert)
    cursor.commit()

    option = int(input('\nPara cadastrar outro usuario digite 1 \n Para listar usuarios cadastrados digite 2 \n Para sair digite 3 \n >>>> '))

    if option == 1:
        pass
    elif option == 2:

        select = pd.read_sql('\nSELECT * FROM Usuarios\n', con)
        print(select)
        opt = int(input('\nDigite 1 para cadastrar outro usuario \n Digite 2 para sair \n >>>>'))

        if opt == 1:
            pass
        else:
            break

    else:
        break