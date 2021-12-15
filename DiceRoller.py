from tkinter import *
import random
from functools import partial


top = Tk()
top.geometry("800x600")


def roll_dice(b1, b2, b3, b4, b5, b6):
    face = random.randrange(6)+1
    #print(face)
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()

    if face==1:
        b1.place(x=30, y=10)
    elif face==2:
        b2.place(x=30, y=10)
    elif face==3:
        b3.place(x=30, y=10)
    elif face==4:
        b4.place(x=30, y=10)
    elif face==5:
        b5.place(x=30, y=10)
    else:
        b6.place(x=30, y=10)
        
        

img1 = PhotoImage(file="dice1.png")
l1 = Label(image=img1)
b1 = Button(top,image=img1)

img2 = PhotoImage(file="dice2.png")
l2 = Label(image=img2)
b2 = Button(top,image=img2)

img3 = PhotoImage(file="dice3.png")
l3 = Label(image=img3)
b3 = Button(top,image=img3)

img4 = PhotoImage(file="dice4.png")
l4 = Label(image=img4)
b4 = Button(top,image=img4)


img5 = PhotoImage(file="dice5.png")
l5 = Label(image=img5)
b5 = Button(top,image=img5)

img6 = PhotoImage(file="dice6.png")
l6 = Label(image=img6)
b6 = Button(top,image=img6)


roll_dice = partial(roll_dice, b1, b2, b3, b4, b5, b6)

b = Button(top, text="Roll", command=roll_dice).place(x=400, y=500)

top.mainloop()
