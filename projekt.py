from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from winsound import *

raam = Tk()
raam.title("Kitarrihäälestaja")
raam.geometry("300x300")
##raam.config(bg='black')

background_image = ImageTk.PhotoImage(Image.open("pilt.jpg"))
background_label = Label(raam, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#standard tuning
a_keel = lambda: PlaySound('helid/standard_a', SND_FILENAME)
e_korge = lambda: PlaySound('helid/standard_e_korge', SND_FILENAME)
d_keel = lambda: PlaySound('helid/standard_d', SND_FILENAME)
g_keel = lambda: PlaySound('helid/standard_g', SND_FILENAME)
b_keel = lambda: PlaySound('helid/standard_b', SND_FILENAME)
e_madal = lambda: PlaySound('helid/standard_e_madal', SND_FILENAME)

#drop d
drop_d_e = lambda: PlaySound('helid/drop_d_e', SND_FILENAME)

#drop c
drop_c_e = lambda: PlaySound('helid/drop_c_e', SND_FILENAME)
drop_c_a = lambda: PlaySound('helid/drop_c_a', SND_FILENAME)
drop_c_d = lambda: PlaySound('helid/drop_c_d', SND_FILENAME)
drop_c_f = lambda: PlaySound('helid/drop_c_f', SND_FILENAME)
drop_c_eelviimane = lambda: PlaySound('helid/drop_c_eelviimane', SND_FILENAME)
drop_c_viimane = lambda: PlaySound('helid/drop_c_viimane', SND_FILENAME)

#drop b
drop_b_a = lambda: PlaySound('helid/drop_b_a', SND_FILENAME)
drop_b_g = lambda: PlaySound('helid/drop_b_g', SND_FILENAME)
drop_b_e = lambda: PlaySound('helid/drop_b_e', SND_FILENAME)
drop_b_e_kor = lambda: PlaySound('helid/drop_b_e_korge_real', SND_FILENAME)
drop_b_d = lambda: PlaySound('helid/drop_b_d', SND_FILENAME)
drop_b_b = lambda: PlaySound('helid/drop_b_b', SND_FILENAME)

#drop a
drop_a_a = lambda: PlaySound('helid/drop_a_a', SND_FILENAME)
drop_a_g = lambda: PlaySound('helid/drop_a_g', SND_FILENAME)
drop_a_e = lambda: PlaySound('helid/drop_a_e', SND_FILENAME)
drop_a_e_kor = lambda: PlaySound('helid/drop_a_e_kor', SND_FILENAME)
drop_a_d = lambda: PlaySound('helid/drop_a_d', SND_FILENAME)
drop_a_b = lambda: PlaySound('helid/drop_a_b', SND_FILENAME)

def ok():
    uus = Toplevel()
    uus.title(variable.get())
    uus.geometry('300x180')
    
    background_image = ImageTk.PhotoImage(Image.open("pilt.jpg"))
    background_label = Label(uus, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    if variable.get() == 'Standard Tuning':
        E = ttk.Button(uus, text="E", command=e_madal)
        E.place(x=100, y=0, width=100)

        A = ttk.Button(uus, text="A", command=a_keel)
        A.place(x=100, y=30, width=100)

        B = ttk.Button(uus, text="D", command=d_keel)
        B.place(x=100, y=60, width=100)

        C = ttk.Button(uus, text="G", command=g_keel)
        C.place(x=100, y=90, width=100)

        D = ttk.Button(uus, text="B", command=b_keel)
        D.place(x=100, y=120, width=100)

        F = ttk.Button(uus, text="E", command=e_korge)
        F.place(x=100, y=150, width=100)

    elif variable.get() == 'Drop D':
        E = ttk.Button(uus, text="D", command=drop_d_e)
        E.place(x=100, y=0, width=100)

        A = ttk.Button(uus, text="A", command=a_keel)
        A.place(x=100, y=30, width=100)

        B = ttk.Button(uus, text="D", command=d_keel)
        B.place(x=100, y=60, width=100)

        C = ttk.Button(uus, text="G", command=g_keel)
        C.place(x=100, y=90, width=100)

        D = ttk.Button(uus, text="B", command=b_keel)
        D.place(x=100, y=120, width=100)

        F = ttk.Button(uus, text="E", command=e_korge)
        F.place(x=100, y=150, width=100)

    elif variable.get() == 'Drop C':
        E = ttk.Button(uus, text="C", command=drop_c_e)
        E.place(x=100, y=0, width=100)

        A = ttk.Button(uus, text="G", command=drop_c_a)
        A.place(x=100, y=30, width=100)

        B = ttk.Button(uus, text="C", command=drop_c_d)
        B.place(x=100, y=60, width=100)

        C = ttk.Button(uus, text="F", command=drop_c_f)
        C.place(x=100, y=90, width=100)

        D = ttk.Button(uus, text="A", command=drop_c_eelviimane)
        D.place(x=100, y=120, width=100)

        F = ttk.Button(uus, text="D", command=drop_c_viimane)
        F.place(x=100, y=150, width=100)

    elif variable.get() == 'Drop B':
        E = ttk.Button(uus, text="B", command=drop_b_e)
        E.place(x=100, y=0, width=100)

        A = ttk.Button(uus, text="F#", command=drop_b_a)
        A.place(x=100, y=30, width=100)

        B = ttk.Button(uus, text="B", command=drop_b_d)
        B.place(x=100, y=60, width=100)

        C = ttk.Button(uus, text="E", command=drop_b_g)
        C.place(x=100, y=90, width=100)

        D = ttk.Button(uus, text="G#", command=drop_b_b)
        D.place(x=100, y=120, width=100)

        F = ttk.Button(uus, text="C#", command=drop_b_e_kor)
        F.place(x=100, y=150, width=100)

    elif variable.get() == 'Drop A':
        E = ttk.Button(uus, text="A", command=drop_a_e)
        E.place(x=100, y=0, width=100)

        A = ttk.Button(uus, text="E", command=drop_a_a)
        A.place(x=100, y=30, width=100)

        B = ttk.Button(uus, text="A", command=drop_a_d)
        B.place(x=100, y=60, width=100)

        C = ttk.Button(uus, text="D", command=drop_a_g)
        C.place(x=100, y=90, width=100)

        D = ttk.Button(uus, text="F#", command=drop_a_b)
        D.place(x=100, y=120, width=100)

        F = ttk.Button(uus, text="B", command=drop_a_e_kor)
        F.place(x=100, y=150, width=100)


variable = StringVar(raam)
variable.set("Standard Tuning")

w = OptionMenu(raam, variable, "Standard Tuning", "Drop D", "Drop C","Drop B","Drop A")
w.pack()

def answer():
    messagebox.showinfo("Quit", "Thank you for using Guitar tuner")
    raam.destroy()

button = Button(raam, text="OK", command=ok)
button.pack()

Button(text='Quit', command=answer).pack(side=BOTTOM)

raam.mainloop()

