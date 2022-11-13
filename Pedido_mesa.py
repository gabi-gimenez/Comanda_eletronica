from tkinter.ttk import*
from tkinter import*
from PIL import Image, ImageTk

#Cores
black = '#000000' #preto
lightGrey = '#909193' #cinza claro
grey = '#181818' #cinza
white = '#f0f3f5' #branco
green = '#40C308' #verde


#interface
win_pedidos = Tk ()
win_pedidos.title("")
win_pedidos.geometry('400x350+500+200')
win_pedidos.configure(background=white)
win_pedidos.resizable(width=FALSE, height=FALSE)

#Importando imagem
pedido_img = Image.open('pedido.png')
pedido_img = pedido_img.resize((20,20))
pedido_img = ImageTk.PhotoImage(pedido_img)
#Titulo
frame_title_pedidos = Frame(win_pedidos,width=400, height=33, bg=green)
frame_title_pedidos.grid(row=0,column=0,pady=0,padx=0)

label_title= Label(frame_title_pedidos, text='Pedido',height=100,anchor=NE, font=('Comic 12 bold'),bg=green,fg=black)
label_title.place(x=35,y=4)

label_table = Label(frame_title_pedidos,height=100,image=pedido_img, compound=LEFT, padx=8, anchor=NE, bg=green)
label_table.place(x=10,y=4)


frame_pedidos= Frame(win_pedidos,width=400, height=400)
frame_pedidos.grid(row=1,column=0,pady=50,padx=0)
frame_pedidos.place(x=20,y=50)

check = Checkbutton(frame_pedidos,text = 'Comida',font=('comic 11'),bg=white,width=10)
check.pack()
frame_pedidos.place(x=50,y=0)


#Botão criar pedido
btn_pedido = Button(frame_pedidos,text = '+',font=('comic 11 bold'),bg=green,width=2)
btn_pedido.pack()
frame_pedidos.place(x=365,y=0)



win_pedidos.mainloop()