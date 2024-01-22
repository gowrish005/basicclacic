import tkinter
from tkinter import *

def add():
    try:
        val1 = int(n1.get())
        val2 = int(n2.get())
        val = val1+val2
        am = "total = "
        fin = str(am)+str(val)
        label.config(text=fin)
    except Exception as e:
        label.config(text="fuck you")

def sub():
    try:
        val2 = int(n2.get())
        val1 = int(n1.get())
        val = val1-val2
        am = "substraction = "
        fin = str(am)+str(val)
        label.config(text=fin)
    except Exception as e:
        label.config(text="fuck off")
def mul():
    try:
        val1 = int(n1.get())
        val2 = int(n2.get())
        val = val1*val2
        am = "multiplication val = "
        fin = str(am)+str(val)
        label.config(text=fin)
    except Exception as e:
        label.config(text="fuck me")

def dev():
    try:
        val1 = int(n1.get())
        val2 = int(n2.get())
        val = val1/val2
        am = "divided = "
        fin = str(am)+str(val)
        label.config(text=fin)
    except Exception as e:
        label.config(text="ur mom")



window = Tk()
window.config(padx=50,pady=50)

#t1= text 1 , t2 = text 2

t1 = Text(window,height=1)
t2 = Text(window,height=1)


sadd = Button(window,text="Add both vaules",command=add,font=('ink free',20,'bold'))
ssub = Button(window,text="substract both values",command=sub,font=('ink free',20,'bold'))
smul = Button(window,text="multiply both vaules",command=mul,font=('ink free',20,'bold'))
sdev = Button(window,text="dived both vaules",command=dev,font=('ink free',20,'bold'))

n1 = Entry(font=('ink free',50,'bold'))
n2 = Entry(font=('ink free',50,'bold'))

label = Label(window,font=('ink free',70,'bold'))

t1.pack()
t1.insert("1.0","1st val")
t1.config(font=("ink free",12,"bold"),state=DISABLED,)

n1.pack()

t2.insert("1.0","2nd val")
t2.config(font=("ink free",12,"bold"),state=DISABLED,)
t2.pack()

n2.pack()

label.pack()

sadd.pack(side=LEFT)
ssub.pack(side=LEFT)
smul.pack(side=RIGHT)
sdev.pack(side=RIGHT)



window.mainloop()