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
# -----------------------H1----------------------- #
nome_empresa = Label(index)
nome_empresa.configure(
    text = "Love Pet",
    bg = '#086788',
    fg = '#FFFFFF',
    font = ('Verdana', 35,'bold')
)
nome_empresa.place(x=390, y=30)


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

index.mainloop()