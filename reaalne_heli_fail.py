<<<<<<< HEAD:reaalne_heli_fail.py
import pyaudio     
import wave

import pyaudio
import numpy as np
from time import sleep
np.set_printoptions(suppress=True) # don't use scientific notation


import numpy as np
from time import sleep
np.set_printoptions(suppress=True) # don't use scientific notation


CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)
TARGET = 2100 # show only this one frequency

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
for i in range(400): #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/2)] # keep only first half
    freq = np.fft.fftfreq(CHUNK,1.0/RATE)
    freq = freq[:int(len(freq)/2)] # keep only first half
    assert freq[-1]>TARGET, "ERROR: increase chunk size"
    val = fft[np.where(freq>TARGET)[0][0]]
    if val > 400:
        print(val)
        sleep(0.2)

# close the stream gracefully

stream.stop_stream()
stream.close()
p.terminate()
=======
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from winsound import *

raam = Tk()
raam.title("Kitarrihäälestaja")
raam.geometry("300x300")

"""
canv = Canvas(raam, height=300, width=300, bg ="white")
canv.grid(row=0, column=0)

img = ImageTk.PhotoImage(Image.open("pilt.jpg"))
canv.create_image(20, 20, anchor=NW, image=img)
canv.pack()
mainloop()
"""
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

def tervita():
    tervitus = '0 väravat '
    messagebox.showinfo(message=tervitus) ##kast

def ok():
    uus = Tk()
    uus.title('valitud')
    uus.geometry('300x300')

    if variable.get() == 'Standard Tuning':
        E = ttk.Button(uus, text="E", command=e_madal)
        E.place(x=0, y=0, width=100)

        A = ttk.Button(uus, text="A", command=a_keel)
        A.place(x=0, y=30, width=100)

        B = ttk.Button(uus, text="D", command=d_keel)
        B.place(x=0, y=60, width=100)

        C = ttk.Button(uus, text="G", command=g_keel)
        C.place(x=0, y=90, width=100)

        D = ttk.Button(uus, text="B", command=b_keel)
        D.place(x=0, y=120, width=100)

        F = ttk.Button(uus, text="E", command=e_korge)
        F.place(x=0, y=150, width=100)

    elif variable.get() == 'Drop D':
        E = ttk.Button(uus, text="D", command=drop_d_e)
        E.place(x=0, y=0, width=100)

        A = ttk.Button(uus, text="A", command=a_keel)
        A.place(x=0, y=30, width=100)

        B = ttk.Button(uus, text="D", command=d_keel)
        B.place(x=0, y=60, width=100)

        C = ttk.Button(uus, text="G", command=g_keel)
        C.place(x=0, y=90, width=100)

        D = ttk.Button(uus, text="B", command=b_keel)
        D.place(x=0, y=120, width=100)

        F = ttk.Button(uus, text="E", command=e_korge)
        F.place(x=0, y=150, width=100)

    elif variable.get() == 'Drop C':
        E = ttk.Button(uus, text="C", command=drop_c_e)
        E.place(x=0, y=30, width=100)

        A = ttk.Button(uus, text="G", command=drop_c_a)
        A.place(x=0, y=30, width=100)

        B = ttk.Button(uus, text="C", command=drop_c_d)
        B.place(x=0, y=60, width=100)

        C = ttk.Button(uus, text="F", command=drop_c_f)
        C.place(x=0, y=90, width=100)

        D = ttk.Button(uus, text="A", command=drop_c_eelviimane)
        D.place(x=0, y=120, width=100)

        F = ttk.Button(uus, text="D", command=drop_c_viimane)
        F.place(x=0, y=150, width=100)


variable = StringVar(raam)
variable.set("Standard Tuning")

w = OptionMenu(raam, variable, "Standard Tuning", "Drop D", "Drop C")
w.pack()

button = Button(raam, text="OK", command=ok)
button.pack()




raam.mainloop()
>>>>>>> 9a103faf50d3a37183bd061141cf8deb4cd0fa5d:projekt.py
