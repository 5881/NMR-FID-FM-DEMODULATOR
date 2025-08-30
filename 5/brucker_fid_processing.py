#!/bin/python
import numpy as np
import nmrglue as ng
from scipy.io.wavfile import write

dict,test=ng.bruker.read(dir="./")
print(test, len(test)/10)
print(test.real, len(test.real)/10)
print(test.imag, len(test.imag)/10)

pdata=np.vstack((test.real, test.imag)).T
print(pdata)
print(max(test.real))
write("5_first_nmm_defect_filter.wav", 20006, pdata.astype(np.int16))

