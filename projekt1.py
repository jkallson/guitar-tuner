from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def tervita():
    tervitus = '0 väravat '
    messagebox.showinfo(message=tervitus) ##kast

def ok():
    uus = Tk()
    uus.title('valitud')
    uus.geometry('300x300')
    
    if variable.get() == 'one':
        D = ttk.Button(uus, text="Mängi", command=tervita)
        D.place(x=0, y=120, width=100)

raam = Tk()
raam.title("Kitarrihäälestaja")
raam.geometry("300x300")

variable = StringVar(raam)
variable.set("one")

w = OptionMenu(raam, variable, "one", "two", "three")
w.pack()

button = Button(raam, text="OK", command=ok)
button.pack()


E = ttk.Button(raam, text="Mängi", command=tervita)
E.place(x=0, y=0, width=100)

A = ttk.Button(raam, text="Mängi", command=tervita)
A.place(x=0, y=30, width=100)

B = ttk.Button(raam, text="Mängi", command=tervita)
B.place(x=0, y=60, width=100)

C = ttk.Button(raam, text="Mängi", command=tervita)
C.place(x=0, y=90, width=100)

D = ttk.Button(raam, text="Mängi", command=tervita)
D.place(x=0, y=120, width=100)

F = ttk.Button(raam, text="Mängi", command=tervita)
F.place(x=0, y=150, width=100)


raam.mainloop()
