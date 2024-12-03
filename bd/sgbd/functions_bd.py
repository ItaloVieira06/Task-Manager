import mysql.connector
from bd.database.data import *

#função de conexão
def conection():
    connection = mysql.connector.connect(
    host = host1,
    user = user1,
    password = password1,
    database = "works"
   )
    
    return connection

#==================================================================================================

#função para inserir no banco de dados
def insertion(Name, Description, Date_Initial, Date_Final):
    creation = """ 
       INSERT INTO tasks(Name, Description, Date_Initial, Date_Final) 
       VALUES(%s, %s, %s, %s) 
    """ 
    values = [Name, Description, Date_Initial, Date_Final] 

    sql = [creation, values] 
    
    return sql


#função
def updation(task_id, Name, Description, Date_Initial, Date_Final):
    edit = """
        UPDATE tasks SET Name = %s, Description = %s, Date_Initial = %s, Date_Final = %s WHERE ID = %s
    """
    values = [Name, Description, Date_Initial, Date_Final, task_id] 

    sql = [edit, values]

    return sql
    


def deletation(task_id):
    take_of = """
        DELETE from tasks WHERE ID = %s
    """
    values = [task_id]

    sql = [take_of, values]

    return sql

#=================================================================================================

def showing():
    shower = """
        SELECT * FROM tasks

    """
    return shower