from scipy.io import wavfile
import numpy as np
from scipy.fft import rfft, rfftfreq, irfft
import matplotlib.pyplot as plt


samplerate, data = wavfile.read('audios/highpitch.wav')
dur = 1
data = np.array([data[i][0] for i in range(samplerate*dur)])
N = samplerate * dur

yf = rfft(data)
xf = rfftfreq(N, 1 / samplerate)

# frequency and amplitude are put into a dict
# now we can see the frequency of the highest amplitude
pop = dict(zip(yf, xf))
print(pop[max(yf)])


plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.plot(xf, np.abs(yf))
plt.xlim(right=samplerate/2)
plt.show()
