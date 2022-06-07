from tkinter import *
from PIL import Image, ImageTk

index = Tk()
index.title("Love Pet")
index.geometry("1024x600")
index.configure(bg = "#086788")
index.resizable(False,False)

# --------------------Função sair-------------------- #
def sairProg():
    index.destroy()

# --------------------Função redimensionar img-------------------- #
def redimensionar(img,x,y):
    rimg = img.resize((x,y),Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(rimg)
    return new_img
img = (Image.open('sair.png'))
img = redimensionar(img, 25, 25)

# -----------------------Class Entry----------------------- #
class botoes:
    def __init__(self, container):
         self.bt = Button (container)
         self.bt.configure(
            bg = '#C4C4C4',
            width= 14,
            height= 2,
            font=('Verdana', 18,'bold')
         )

# -------------------Funções para abrir as páginas-------------------#
def Open_cadPes():
    print('calma bb')

def Open_adoc():
    print('calma bb')

def Open_geren():
    print('calma bb')

def Open_cadPet():
    print('calma bb')

def Open_tabPet():
    print('calma bb')

def Open_cadCli():
    print('calma bb')


# -----------------------Nome da empresa----------------------- #
nome_empresa = Label(index)
nome_empresa.configure(
    text = "Love Pet",
    bg = '#086788',
    fg = '#FFFFFF',
    font = ('Verdana', 40,'bold')
)
nome_empresa.place(x=378, y=30)

sair_botao = Button(index)
sair_botao.configure(
    image= img,
    bg = '#C4C4C4',
    width= 30,
    height= 40,
    relief = RAISED,
    command= sairProg
)
sair_botao.place(x=978, y=20)

#-----------Menu---------#
#   --lado esquerdo--    #
cadPes_but = botoes(index)
cadPes_but.bt.configure(text='Cadastro', command= Open_cadPes)
cadPes_but.bt.place(x=238, y=160)

adoc_but = botoes(index)
adoc_but.bt.configure(text='Adoção', command= Open_adoc)
adoc_but.bt.place(x=238, y=260)

geren_but = botoes(index)
geren_but.bt.configure(text='Gerenciamento', command= Open_geren)
geren_but.bt.place(x=238, y=360)

#   --lado Direito--    #

cadPet_but = botoes(index)
cadPet_but.bt.configure(text='Cadastra Pet', command= Open_cadPet)
cadPet_but.bt.place(x=538, y=160)

tabPet_but = botoes(index)
tabPet_but.bt.configure(text='Tabela de Pets', command= Open_tabPet)
tabPet_but.bt.place(x=538, y=260)

cadCli_but = botoes(index)
cadCli_but.bt.configure(text='Cadastrar Clínicas', command= Open_cadCli)
cadCli_but.bt.place(x=538, y=360)

index.mainloop()