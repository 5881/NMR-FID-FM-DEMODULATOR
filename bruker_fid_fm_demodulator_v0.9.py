#!/bin/python
import numpy as np
import nmrglue as ng
import sys
from scipy.io.wavfile import write


def bruker_fm_demodulator(directory):
	if (directory[-1]=='/'):
		temp=directory[:-1]
	else:
		temp=directory
	name=temp.split('/')[-1]+'.wav'

	dict,test=ng.bruker.read(dir=directory)
	duration=dict['acqus']["TD"]/(2*dict['acqus']["SW_h"])
	I=test.real
	Q=test.imag
	y=(I[1:]*Q[:-1]-Q[1:]*I[:-1])/(I[1:]**2+Q[1:]**2+0.001)
	SR=int(len(y)//duration)
	#print("demod",y,len(I),len(Q),len(y),SR)
	write(name, SR, y.astype(np.float32))

for directory in sys.argv[1:]:
	bruker_fm_demodulator(directory)
