from tkinter.ttk import*
from tkinter import*
from PIL import Image, ImageTk


#Cores
black = '#000000' #preto
lightGrey = '#909193' #cinza claro
grey = '#181818' #cinza
white = '#f0f3f5' #branco
green = '#40C308' #verde

class Interface ():

    def __init__(self,windown):
        self.win = windown
        self.win.tilte('')
        self.win.geometry('300x200+500+200')
        self.win.configure(background=white)
        self.win.resizable(width=FALSE, height=FALSE)

    def import_img (self,img):

        self.img = img
        self.img = Image.open(img)
        self.img = self.img.resize((25,25))
        self.img = ImageTk.PhotoImage(self.img)





label_title = i.label_negrito(frame_title,'Mesas',12,green,black,0,0,0,0,35,4)
#Titulo
frame_title = Frame(win_table,width=400, height=33, bg=green)
frame_title.grid(row=0,column=0,pady=0,padx=0)


label_table = Label(frame_title,height=100,image=i.import_img('cardapio.png'), compound=LEFT, padx=8, anchor=NE, bg=green)
label_table.place(x=5,y=4)


#box mesa

frame_table= Frame(win_table,width=50, height=50, bg=green)
frame_table.grid(row=1,column=0,pady=50,padx=0)
frame_table.place(x=20,y=50)

#Botão criar mesa
btn_table = Button(frame_table, text = '+',font=('comic 14 bold'),bg=green,width=2)
btn_table.pack()


#box cardapio

frame_cardapio= Frame(win_table,width=50, height=50, bg=green)
frame_cardapio.grid(row=1,column=0,pady=50,padx=0)
frame_cardapio.place(x=20,y=50)

#Botão cardapio
btn_cardapio = Button(frame_cardapio,image=cardapio_img,font=('comic 14 bold'),bg=green,width=27, height=27)
btn_cardapio.pack()
frame_cardapio.place(x=265,y=0)

#box pedido

frame_pedido= Frame(win_table,width=50, height=50, bg=green)
frame_pedido.grid(row=1,column=0,pady=50,padx=0)
frame_pedido.place(x=20,y=50)

#Botão pedido
btn_pedido = Button(frame_pedido,image=pedido_img,font=('comic 14 bold'),bg=green,width=29, height=27)
btn_pedido.pack()
frame_pedido.place(x=230,y=0)



if __name__ == '__main__':
    window = Tk()
    application = Interface(window)
    window.mainloop()


