from bd.database.create_bd import *
from bd.sgbd.functions_bd import *

#===========================================================================================================

#função para criar dados para o bd
def creative(Name, Description, Date_Initial, Date_Final):
 conection()
 cursor = connection.cursor()
 command_data = insertion(Name, Description, Date_Initial, Date_Final)
 cursor.execute(command_data[0], command_data[1])

 connection.commit()

#==========================================================================================================

#função para editar dados do bd
def editor(task_id, Name, Description, Date_Initial, Date_Final):
 conection()
 cursor = connection.cursor()
 command_data = updation(task_id, Name, Description, Date_Initial, Date_Final)
 cursor.execute(command_data[0], command_data[1])

 connection.commit()

#============================================================================================================

#função para remover dados do bd
def remover(task_id):
 conection()
 cursor = connection.cursor()
 command_data = deletation(task_id)
 cursor.execute(command_data[0], command_data[1])

 connection.commit()

#============================================================================================================

#função para pegar os dados do bd e que depois será usado para criar uma tabela
def showing2():
 conection()
 cursor = connection.cursor()
 cursor.execute(showing())
 rows = cursor.fetchall()

 return rows
