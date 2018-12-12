from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from winsound import *
from random import randint 

raam = Tk()
raam.title("Kitarrihäälestaja")
raam.geometry("300x300")

background_image = ImageTk.PhotoImage(Image.open("pilt.jpg"))
background_label = Label(raam, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


a_keel = lambda: PlaySound('standard_a.wav', SND_FILENAME)
e_korge = lambda: PlaySound('standard_e_korge.wav', SND_FILENAME)
d_keel = lambda: PlaySound('standard_d', SND_FILENAME)
g_keel = lambda: PlaySound('standard_g', SND_FILENAME)
b_keel = lambda: PlaySound('standard_b', SND_FILENAME)
e_madal = lambda: PlaySound('standard_e_madal', SND_FILENAME)
drop_d_e = lambda: PlaySound('drop_d_e', SND_FILENAME)
drop_c_e = lambda: PlaySound('drop_c_e', SND_FILENAME)
drop_c_a = lambda: PlaySound('drop_c_a', SND_FILENAME)
drop_c_d = lambda: PlaySound('drop_c_d', SND_FILENAME)
drop_c_f = lambda: PlaySound('drop_c_f', SND_FILENAME)
drop_c_eelviimane = lambda: PlaySound('drop_c_eelviimane', SND_FILENAME)
drop_c_viimane = lambda: PlaySound('drop_c_viimane', SND_FILENAME)
laul1 = lambda: PlaySound("Stairway", SND_FILENAME)
laul2 = lambda: PlaySound("Nothing", SND_FILENAME)
laul3 = lambda: PlaySound("Laporte", SND_FILENAME)

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


def varia():
    laused = ["Esimene kitarr loodi Vana-Egiptuses", "Maailma suurim kitarr on 13 meetrit pikk", "Maailma väikseim kitarr on 10 mikromeetrit pikk","Maailma kalleim kitarr maksab 2,8 miljonit dollarit","Inglismaal abiellus üks muusik oma kitarriga","Kitarrifirma Ibanez tõi esimest korda turule 7 ja 8 keelelised kitarrid", "Kõige pikem järjestikune kitarrimängimine kestis 114 tundi","Esimese elektrikitarri tegi Gibson 1936 aastal","Jimi Hendrix mängis kitarri tagurpidi, sest ta oli vasakukäeline","Fenderi kitarritööstus teeb päevas 90 000 keelt"]
    suvaline = randint(1,10)
    
    for arv in range(1,11):
        if arv == suvaline:
            messagebox.showinfo('Varia',laused[arv-1])
            
        
    
varia = ttk.Button(raam, text="Varia", command=varia)
varia.place(x=100, y=230, width=100)

def akordid():
    uus = Toplevel()
    uus.title("Akordid")
    uus.geometry('1000x321')
    background_image = ImageTk.PhotoImage(Image.open("akordid.jpg"))
    background_label = Label(uus, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
akordid = ttk.Button(raam, text="Akordid", command=akordid)
akordid.place(x=100, y=200, width=100)

def muusika():
    uus = Toplevel()
    uus.title(variable.get())
    uus.geometry('300x300')
    background_image = ImageTk.PhotoImage(Image.open("pilt.jpg"))
    background_label = Label(uus, image=background_image)
    background_label.image = background_image
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    Stairway = ttk.Button(uus, text="Stairway to heaven", command=laul1)
    Stairway.place(x=0, y=0, width=200)

    Nothing = ttk.Button(uus, text="Nothing else matters", command=laul2)
    Nothing.place(x=0, y=30, width=200)

    Laporte = ttk.Button(uus, text="Black widow of la porte", command=laul3)
    Laporte.place(x=0, y=60, width=200)
    
    
laulud = ttk.Button(raam, text="♪♫♬", command=muusika)
laulud.place(x=270, y=275, width=30)

button = Button(raam, text="OK", command=ok)
button.pack()

Button(text='Quit', command=answer).pack(side=BOTTOM)


raam.mainloop()

