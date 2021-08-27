import matplotlib.pyplot as plt
import numpy as np
import wave

volume = 0.5     # range [0.0, 1.0]
fs = 48000       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 76.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float16)
plt.plot(samples)
plt.show()
# for paFloat32 sample values must be in range [-1.0, 1.0]

# play. May repeat with different volume values (if done interactively) 
with wave.open('audios/tosinewave.wav', 'wb') as sine:
    sine.setnchannels(1)
    sine.setsampwidth(1)
    sine.setframerate(48000)
    sine.writeframes(samples)
