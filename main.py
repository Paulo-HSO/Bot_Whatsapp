import tkinter
from tkinter import ttk

def contact_select():
    quantidadeContatos = int(Quantidade_contatos_spinbox.get())

    contato_nome = tkinter.LabelFrame(frame, text="Nome dos Contatos")
    contato_nome.grid(row= 1, column= 0)
    
    i = 0
    while i < quantidadeContatos: 
        nomes = tkinter.Label(contato_nome, text= f"Contato {i+1}")
        nomes_input = ttk.Entry(contato_nome)
        nomes.grid(row=i, column=0, pady= 10, padx= 10)
        nomes_input.grid(row=i, column=1, pady= 10, padx= 10)
        i+=1

    print("Quantidade de contatos: ", quantidadeContatos)

def botStarted():
    print("Start destruction!")

window = tkinter.Tk()
window.title("Bot de Mensagens para Whatsapp")

frame = tkinter.Frame(window)
frame.pack()

# Selecionando os contatos que receberam a mensagem
contato_frame = tkinter.LabelFrame(frame, text="Contatos")
contato_frame.grid(row= 0, column= 0, padx=20, pady=20)

Quantidade_contatos = tkinter.Label(contato_frame, text="Quantidade de contatos")
Quantidade_contatos_spinbox = ttk.Spinbox(contato_frame, from_= 1, to= 20)
Quantidade_contatos.grid(row=0, column=0)
Quantidade_contatos_spinbox.grid(row=1, column=0)
Quantidade_contatos_button = tkinter.Button(contato_frame, text="Confirmar", command= contact_select)
Quantidade_contatos_button.grid(row=2, column=0, sticky="news", padx=10, pady=10)

for widget in contato_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = tkinter.Button(frame, text="Enviar mensagem", command= botStarted)
button.grid(row=2, column=0, sticky="news", padx=20, pady=20)

window.mainloop()