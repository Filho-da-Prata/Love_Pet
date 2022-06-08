from msilib.schema import RadioButton
from tkinter import *
import tkinter as tk

window = Tk()
window.title("Love Pet")
window.geometry("1024x600")
window.configure(bg="#086788")
window.resizable(False, False)

# -----------------------Class Entry----------------------- #

class entrada:
    def __init__(self, container):
        self.et = Entry(container)
        self.et.configure(
            bg='#C4C4C4',
            fg='black',
            width=30,
            font=('Verdana', 13)
        )

# -----------------------Class Label----------------------- #

class textos:
    def __init__(self, container):
        self.lb = Label(container)
        self.lb.configure(
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 17, 'bold')
        )

# -----------------------Class Canvas----------------------- #

class Mypage(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        self.canvas = Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.scroll_bar = Scrollbar(
            self, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.scroll_bar.set)

        self.internal_frame = Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.internal_frame, anchor='nw')

        self.__build()
        self.internal_frame.update_idletasks()

        self.config(width=2048, height=900)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def __build(self):
        #---- criando a Janela ----#
        janela = Frame(self.internal_frame)
        janela.configure(
            bg="#086788",
            width=2048,
            height=900,
            highlightbackground="#086788",
            highlightthickness='0px'
        )
        janela.pack(anchor='center')

    #---- titulo tela ----#

        nome_empresa = Label(janela)
        nome_empresa.configure(
            text="CADASTRO",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 35, 'bold')
        )
        nome_empresa.place(x=358, y=10)

    #---- Criando Label's da tela ----#
        nome_box = textos(janela)
        nome_box.lb.configure(text='Nome:')
        nome_box.lb.place(x=275, y=104)

        cpf_box = textos(janela)
        cpf_box.lb.configure(text='CPF:')
        cpf_box.lb.place(x=300, y=146)

        email_box = textos(janela)
        email_box.lb.configure(text='E-mail:')
        email_box.lb.place(x=267, y=184)

        tel_box = textos(janela)
        tel_box.lb.configure(text='Telefone:')
        tel_box.lb.place(x=237, y=224)

        senh_box = textos(janela)
        senh_box.lb.configure(text='Crie uma senha:')
        senh_box.lb.place(x=150, y=284)

        senConf_box = textos(janela)
        senConf_box.lb.configure(text='Confirme a senha:')
        senConf_box.lb.place(x=122, y=324)

        end_box = Label(janela)
        end_box.configure(
            text="Endereço:",
            bg='#086788',
            fg='#FFFFFF',
            font=('Verdana', 20, 'bold')
        )
        end_box.place(x=425, y=394)

        #---- Criando Label's endereço ----#

        rua_box = textos(janela)
        rua_box.lb.configure(text='Rua:')
        rua_box.lb.place(x=296, y=477)

        num_box = textos(janela)
        num_box.lb.configure(text='Número:')
        num_box.lb.place(x=245, y=517)

        bairro_box = textos(janela)
        bairro_box.lb.configure(text='Bairro:')
        bairro_box.lb.place(x=267, y=557)

        cid_box = textos(janela)
        cid_box.lb.configure(text='Cidade:')
        cid_box.lb.place(x=260, y=597)

        Tp_box = textos(janela)
        Tp_box.lb.configure(text='Tipo de Cadastro:', font=('Verdana', 15, 'bold'))
        Tp_box.lb.place(x=80, y=647)

    #---- Criando Radialbutton's da tela ----#
        radioValue = tk.IntVar()
        n1  = Radiobutton(janela)
        n1.configure(text='Voluntario', variable= radioValue, value= 1, bg='#086788', fg='#FFFFFF', font=('Verdana', 13, 'bold'))
        n1.place(x= 290, y=650)

        n2  = Radiobutton(janela)
        n2.configure(text='Adotante', variable= radioValue, value= 2, bg='#086788', fg='#FFFFFF', font=('Verdana', 13, 'bold'))
        n2.place(x= 290, y=675)

        n3  = Radiobutton(janela)
        n3.configure(text='Ambos', variable= radioValue, value= 3, bg='#086788', fg='#FFFFFF', font=('Verdana', 13, 'bold'))
        n3.place(x= 290, y=700)


    #---- Criando Entry's da tela ----#
        nome_ent = entrada(janela)
        nome_ent.et.place(x=370, y=112)

        cpf_ent = entrada(janela)
        cpf_ent.et.place(x=370, y=152)

        email_ent = entrada(janela)
        email_ent.et.place(x=370, y=192)

        tel_ent = entrada(janela)
        tel_ent.et.place(x=370, y=232)

        sen_ent = entrada(janela)
        sen_ent.et.place(x=370, y=292)

        senConf_ent = entrada(janela)
        senConf_ent.et.place(x=370, y=332)

        #---- Criando Entry's endereço ----#

        rua_ent = entrada(janela)
        rua_ent.et.place(x=370, y=484)

        num_ent = entrada(janela)
        num_ent.et.place(x=370, y=524)

        bairro_ent = entrada(janela)
        bairro_ent.et.place(x=370, y=564)

        cid_ent = entrada(janela)
        cid_ent.et.place(x=370, y=604)

    #---- Criando Button da tela ----#
        bt = Button(janela)
        bt.configure(
            text='Confirmar',
            bg='#C4C4C4',
            width=14,
            height=1,
            font=('Verdana', 20, 'bold')
        )
        bt.place(x= 350, y=760)


cadastro = Mypage(window)

window.mainloop()
