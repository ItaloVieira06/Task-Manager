import mysql.connector
from bd.database.data import *

#================================================================================================================================

#conexão com o mysql
connection = mysql.connector.connect(
    host = host1,
    user = user1,
    password = password1
)

#================================================================================================================================

#criação do banco de dados
cursor = connection.cursor()
cursor.execute("create database if not exists works")

#conexão com o banco de dados
connection = mysql.connector.connect(
    host = host1,
    user = user1,
    password = password1,
    database = "works"
   )

#================================================================================================================================

#função para criação de tabela
def table():
    create = """
     CREATE TABLE if not exists tasks(
      ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
      Name VARCHAR(100), 
      Description VARCHAR(100), 
      Date_Initial VARCHAR(50),
      Date_Final VARCHAR(50)
      )
    """
    return create

#criação de tabela
cursor = connection.cursor()
cursor.execute(table())
connection.commit()

#=====================================================================================================================================