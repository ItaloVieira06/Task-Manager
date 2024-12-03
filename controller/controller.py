from tkinter import *
from tkinter import messagebox

from bd.sgbd.tasks_bd import *

#=========================================================================================================================================

#controlador para criar dados para o bd
def send1(Entry1, Entry2, Entry3, Entry4):
 Name = Entry1.get()
 Description = Entry2.get()
 Date_Initial = Entry3.get()
 Date_Final = Entry4.get()

 list1 = [Name, Description, Date_Final, Date_Initial]
 minimum = list(map(lambda list1: len(list1), list1))
 minimum = min(minimum)
 if (min == 0):
    messagebox("Erro!", "Você deixou um campo em branco!")
 else:
  creative(Name, Description, Date_Initial, Date_Final)

#==========================================================================================================================================

#controlador para editar dados para o bd
def send2(Entry1, Entry2, Entry3, Entry4, Entry5):
 task_id = Entry1.get()
 Name = Entry2.get()
 Description = Entry3.get()
 Date_Initial = Entry4.get()
 Date_Final = Entry5.get()

 list1 = [task_id, Name, Description, Date_Final, Date_Initial]
 minimum = list(map(lambda list1: len(list1), list1))
 minimum = min(minimum)
 if (min == 0):
    messagebox("Erro!", "Você deixou um campo em branco!")
 else:
   editor(task_id, Name, Description, Date_Initial, Date_Final)

#==========================================================================================================================================

#controlador para apagar dados do bd
def send3(Entry):
   task_id = Entry.get()
   yesno = messagebox.askyesno("Atenção!", "Você tem certeza que quer excluir esta tarefa?")
   if yesno == True:
    remover(task_id)

#==========================================================================================================================================
