from tkinter import *
from tkinter import ttk

from bd.sgbd.tasks_bd import showing2

#janela que mostra as tarefas atuais no banco de dados
def info_screen_():
 inf_screen = Toplevel()
 inf_screen.title("Agenda de Tarefas")
 
 #receptor dos dados que serão colocados nas linhas
 rows = showing2()
 
 #criação da tabela
 table = ttk.Treeview(inf_screen)

 #configuração das colunas da tabela
 table["columns"] = ("ID", "Name", "Description", "Initial Date", "Deadline")

 
 table.heading("ID", text="ID", anchor=CENTER)
 table.heading("Name", text="Name", anchor=CENTER)
 table.heading("Description", text="Description", anchor=CENTER)
 table.heading("Initial Date", text="Initial Date", anchor=CENTER)
 table.heading("Deadline", text="Deadline", anchor=CENTER)
 
 #inserção dos dados de acordo com o ID deles, funcionando até acabar os valores
 for i in rows:
  table.insert('', 'end', values= i)

 table.pack()
