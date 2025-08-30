#!/bin/python
import numpy as np
import nmrglue as ng
from scipy.io.wavfile import write

dict,test=ng.bruker.read(dir="./")
print(test, len(test)/6.5)
print(test.real, len(test.real)/6.5)
print(test.imag, len(test.imag)/6.5)

pdata=np.vstack((test.real, test.imag)).T
print(pdata)
print(max(test.real))
write("test12.wav", 40323, pdata.astype(np.int16))
