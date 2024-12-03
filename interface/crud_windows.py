from tkinter import *
from controller.controller import *
from interface.info_screen import info_screen_

#======================================================================================================================================

#janela para criação de tarefa
def create():
    create = Toplevel()
    create.title("Criar Tarefa")
    create.geometry("1400x600")

    tittle2 = Label(create, text = "Digite o nome da tarefa: ")
    tittle2.grid(column=0, row=0, padx=100, pady=25)
    Name = Entry(create, width=50)
    Name.grid(column=0, row=1, padx=100, pady=25)
    
    tittle3 = Label(create, text = "Digite a descrição da tarefa: ")
    tittle3.grid(column=2, row=0, padx=100, pady=25)
    Description = Entry(create, width=75)
    Description.grid(column=2, row=1, padx=100, pady=25)

    tittle4 = Label(create, text = "Digite a data inicial: ")
    tittle4.grid(column=0, row=2, padx=100, pady=25)
    Date_Initial = Entry(create, width=10)
    Date_Initial.grid(column=0, row=3, padx=100, pady=25)

    tittle5 = Label(create, text = "Digite a data final da tarefa: ")
    tittle5.grid(column=2, row=2, padx=100, pady=25)
    Date_Final = Entry(create, width=10)
    Date_Final.grid(column=2, row=3, padx=100, pady=2)

    send = Button(create, text="Enviar Tarefa", command=lambda: send1(Name, Description, Date_Initial, Date_Final))
    send.grid(column=1, row=4, padx=100, pady=25)

#====================================================================================================================================

#janela para edição de tarefas
def edit():
    info_screen_()
    edit = Toplevel()
    edit.title("Editar Tarefa")
    edit.geometry("1600x800")

    tittle1 = Label(edit, text = "Digite o Id da tarefa que deseja editar: ")
    tittle1.grid(column=1, row=0, padx=100, pady=25)
    task_id = Entry(edit, width=10)
    task_id.grid(column=1, row=1, padx=100, pady=25)

    tittle2 = Label(edit, text = "Digite o novo nome da tarefa: ")
    tittle2.grid(column=0, row=2, padx=100, pady=25)
    Name = Entry(edit, width=50)
    Name.grid(column=0, row=3, padx=100, pady=25)
    
    tittle3 = Label(edit, text = "Digite a nova descrição da tarefa: ")
    tittle3.grid(column=2, row=2, padx=100, pady=25)
    Description = Entry(edit, width=75)
    Description.grid(column=2, row=3, padx=100, pady=25)

    tittle4 = Label(edit, text = "Digite a nova data inicial: ")
    tittle4.grid(column=0, row=4, padx=100, pady=25)
    Date_Initial = Entry(edit, width=10)
    Date_Initial.grid(column=0, row=5, padx=100, pady=25)


    tittle5 = Label(edit, text = "Digite a nova data final da tarefa: ")
    tittle5.grid(column=2, row=4, padx=100, pady=25)
    Date_Final = Entry(edit, width=10)
    Date_Final.grid(column=2, row=5, padx=100, pady=25)

    send = Button(edit, text="Enviar Tarefa", command=lambda: send2(task_id, Name, Description, Date_Initial, Date_Final))
    send.grid(column=1, row=6, padx=100, pady=25)

#=====================================================================================================================================

#janelas para exclusão de tarefas
def exclude():
    info_screen_()
    exclude = Toplevel()
    exclude.title("Excluir Tarefa")
    exclude.geometry("550x300")

    tittle = Label(exclude, text = "Digite o Id da tarefa que deseja excluir e depois aperte o botão: ")
    tittle.grid(column=0, row=0, padx=100, pady=25)

    task_id = Entry(exclude, width=10)
    task_id.grid(column=0, row=1, padx=100, pady=25)

    send = Button(exclude, text="Apagar Tarefa", command=lambda: send3(task_id))
    send.grid(column=0, row=2, padx=100, pady=25)

#=====================================================================================================================================