from tkinter import *
from tkinter import ttk
from tkinter import messagebox



from PIL import Image, ImageTk



raam = Tk()
raam.title("Kitarrihäälestaja")
raam.geometry("300x300")


canv = Canvas(raam, height=300, width=300, bg ="white")
canv.grid(row=0, column=0)

background_image=tk.PhotoImage("pilt.jpg")
background_label = tk.Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

mainloop()

def tervita():
    tervitus = '0 väravat '
    messagebox.showinfo(message=tervitus) ##kast

def ok():
    uus = Tk()
    uus.title('valitud')
    uus.geometry('300x300')
    
    if variable.get() == 'one':
        E = ttk.Button(uus, text="Mängi", command=tervita)
        E.place(x=0, y=0, width=100)

        A = ttk.Button(uus, text="Mängi", command=tervita)
        A.place(x=0, y=30, width=100)

        B = ttk.Button(uus, text="Mängi", command=tervita)
        B.place(x=0, y=60, width=100)

        C = ttk.Button(uus, text="Mängi", command=tervita)
        C.place(x=0, y=90, width=100)

        D = ttk.Button(uus, text="Mängi", command=tervita)
        D.place(x=0, y=120, width=100)

        F = ttk.Button(uus, text="Mängi", command=tervita)
        F.place(x=0, y=150, width=100)
        

variable = StringVar(raam)
variable.set("one")

w = OptionMenu(raam, variable, "one", "two", "three")
w.pack()

button = Button(raam, text="OK", command=ok)
button.pack()




F = ttk.Button(raam, text="Mängi", command=ok)
F.place(x=0, y=150, width=100)


background_label.photo=background
raam.mainloop()
