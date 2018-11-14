from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mp3play import *


def tervita():
    tervitus = '0 väravat '
    messagebox.showinfo(message=tervitus) ##kast


raam = Tk()
raam.title("Kitarrihäälestaja")
raam.geometry("300x100")


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

madal_e = mp3play.load("standard_e_korge.mp3"); play=lambda :madal_e.play()
F = ttk.Button(raam, text="Mängi", command=play)
F.place(x=0, y=150, width=100)


raam.mainloop()
