
import pyaudio     
import wave

import pyaudio
import numpy as np
from time import sleep
np.set_printoptions(suppress=True) 


import numpy as np
from time import sleep
np.set_printoptions(suppress=True) 


CHUNK = 4096
RATE = 44100
TARGET = 2100 

p=pyaudio.PyAudio() 
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
for i in range(400): 
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/2)] 
    freq = np.fft.fftfreq(CHUNK,1.0/RATE)
    freq = freq[:int(len(freq)/2)] 
    assert freq[-1]>TARGET, "ERROR: increase chunk size"
    val = fft[np.where(freq>TARGET)[0][0]]
    if val > 400:
        print(val)
        sleep(0.2)



stream.stop_stream()
stream.close()
p.terminate()