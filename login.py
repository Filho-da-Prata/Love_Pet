from tkinter import *

login = Tk()
login.title("Login")
login.geometry("1024x600")
login.configure(bg="#086788")
login.resizable(False, False)
# -----------------------Class Entry----------------------- #


class entrada:
    def __init__(self, container):
        self.et = Entry(container)
        self.et.configure(
            bg='#C4C4C4',
            fg='black',
            width=20,
            font=('Verdana', 20)
        )

# -----------------------Função Get----------------------- #


def acesso_login():
    get_senha = entrada_senha.et.get()
    get_email = entrada_email.et.get()
    print(get_senha, get_email)


# -----------------------Menus----------------------- #
menubar = Menu(login)
Ajuda = Menu(menubar)
Ajuda.configure(tearoff=0)
menubar.add_cascade(label="Ajuda", menu=Ajuda)
Ajuda.add_command(label="Sobre")

# -----------------------Elementos de acesso----------------------- #
# -----------------------Login----------------------- #
text_box = Label(login)
text_box.configure(
    text="Login:",
    bg='#086788',
    fg='#FFFFFF',
    font=('Verdana', 35, 'bold')
)
text_box.pack(side=TOP, padx=10, pady=60, anchor='center')

# -----------------------e-mail----------------------- #
email_box = Label(login)
email_box.configure(
    text="E-mail:",
    bg='#086788',
    fg='#FFFFFF',
    font=('Verdana', 25, 'bold')
)
email_box.pack(side=TOP, anchor='center')

entrada_email = entrada(login)
entrada_email.et.pack(side=TOP, padx=10, pady=10, anchor='center')

# -----------------------Senha----------------------- #
senha_box = Label(login)
senha_box.configure(
    text="Senha:",
    bg='#086788',
    fg='#FFFFFF',
    font=('Verdana', 25, 'bold')
)
senha_box.pack(side=TOP, anchor='center')

entrada_senha = entrada(login)
entrada_senha.et.configure(show='*')
entrada_senha.et.pack(side=TOP, padx=10, pady=10, anchor='center')

# -----------------------Acesso----------------------- #
botao_acesso = Button(login)
botao_acesso.configure(
    text='Acessar',
    bg='#C4C4C4',
    fg='black',
    font=('Verdana', 20, 'bold'),
    width=7,
    height=1,
    activebackground='black',
    command=acesso_login
)
botao_acesso.pack(side=TOP, padx=10, pady=10, anchor='center')

login.config(menu=menubar)

login.mainloop()
