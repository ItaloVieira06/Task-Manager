from interface.crud_windows import *
from tkinter import *


#janela principal / main do projeto
main = Tk()
main.title("Gerenciador de Tarefas")
main.geometry("1000x400")

tittle = Label(main, text = "Selecione a opção à sua escolha abaixo")
tittle.grid(column=1, row=0, padx=100, pady=25)

create_button = Button(main, text="Criar Tarefa", command= lambda:  create())
create_button.grid(column=0, row=1, padx=100, pady=25)

edit_button = Button(main, text="Editar Tarefa", command= lambda:  edit())
edit_button.grid(column=2, row=1, padx=100, pady=25)

exclude_button = Button(main, text="Apagar Tarefa", command= lambda: exclude())
exclude_button.grid(column=0, row=2, padx=100, pady=25)

show_button = Button(main, text="Ver Tarefas", command= lambda: info_screen_())
show_button.grid(column=2, row=2, padx=100, pady=25)

main.mainloop()