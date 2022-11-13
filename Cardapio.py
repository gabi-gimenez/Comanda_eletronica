from tkinter.ttk import*
from tkinter import*
from PIL import Image, ImageTk

#Cores
black = '#000000' #preto
lightGrey = '#909193' #cinza claro
grey = '#181818' #cinza
white = '#f0f3f5' #branco
green = '#40C308' #verde



class interface ():

    def __init__(self,windown):
        self.win = windown
        self.win.title('')
        self.win.geometry('400x350+500+200')
        self.win.configure(background=white)
        self.win.resizable(width=FALSE, height=FALSE)

    
    
        #Titulo
        frame_title_cardapio = Frame(self.win,width=400, height=33, bg=green)
        frame_title_cardapio.grid(row=0,column=0,pady=0,padx=0)
        frame_title_cardapio = Frame(self.win,width=400, height=33, bg=green)
        frame_title_cardapio.grid(row=0,column=0,pady=0,padx=0)

        #Importando imagem
        cardapio_img = Image.open('cardapio.png')
        cardapio_img = cardapio_img.resize((20,20))
        cardapio_img = ImageTk.PhotoImage(cardapio_img)


        label_title= Label(frame_title_cardapio, text='Cardapio',height=100,anchor=NE, font=('Comic 12 bold'),bg=green,fg=black)
        label_title.place(x=35,y=4)

        label_table = Label(frame_title_cardapio,height=100,image=cardapio_img, compound=LEFT, padx=8, anchor=NE, bg=green)
        label_table.place(x=10,y=4)

        
     
        #Imagem cardapio
        frame_cardapio= Frame(self.win,width=400, height=400)
        frame_cardapio.grid(row=1,column=0,pady=50,padx=0)
        frame_cardapio.place(x=20,y=50)
       
        #Botão criar pedido
        btn_pedido = Button(frame_cardapio,text = '+',font=('comic 11 bold'),bg=green,width=2)
        btn_pedido.pack()
        frame_cardapio.place(x=365,y=0)






if __name__ == '__main__':
    windown = Tk()
    application = interface(windown)
    windown.mainloop()

