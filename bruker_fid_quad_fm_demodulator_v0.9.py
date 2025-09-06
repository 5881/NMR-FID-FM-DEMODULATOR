#!/bin/python
#Alexandr Belyy 29 aug 2025
#Brucker fid FM demodulator
#usage:
#$./brucker_fid_quad_fm_demodulator_v0.9.py path_to_fid
import numpy as np
import nmrglue as ng
import sys
from scipy.io.wavfile import write

def brucker_fm_demodulator(directory):
	if (directory[-1]=='/'):
		temp=directory[:-1]
	else:
		temp=directory
	name=temp.split('/')[-1]+'_quad.wav'

	dict,data=ng.bruker.read(dir=directory)
	duration=dict['acqus']["TD"]/(2*dict['acqus']["SW_h"])
	y=0.5*np.angle(data[:-1]*np.conj(data[1:]))
	SR=int(len(y)//duration)
	#print("demod",y,len(I),len(Q),len(y),SR)
	write(name, SR, y.astype(np.float32))

for directory in sys.argv[1:]:
	brucker_fm_demodulator(directory)
