import sys
sys.path.append('/Users/seffka/DSPMA/sms-tools/software/models/')
from utilFunctions import wavread, wavwrite
from scipy.signal import get_window
import matplotlib.pyplot as plt
import numpy as np
import os
from os import listdir
from os.path import isfile, join, splitext
import essentia
import essentia.standard

def giveNormalizer(x):
	replayGain = essentia.standard.ReplayGain()
	norm = 0.99
	y=np.zeros(2550, dtype=np.float32)
	y[:len(x)] = x
	while (replayGain(y * norm) < -14):
		norm -= 0.001
	return norm

replayGain = essentia.standard.ReplayGain()
rms = essentia.standard.Larm(power = 2)
larm = essentia.standard.Larm()
leq = essentia.standard.Leq()
loudness = essentia.standard.Loudness()
f = [f for f in listdir('hacked') if isfile(join('hacked', f)) and splitext(join('.', f))[1] == '.wav' and 'intro.wav' not in f and '_16_' in f]
for file in f:
	loader = essentia.standard.MonoLoader(filename=join('hacked', file))
	x = loader()
	#print file, '1) max:', max(x), ', rms: ', rms(x), ' larm: ', larm(x), ' leq: ', leq(x), ' loudness: ', loudness(x)
	x = x / max(x)
	print file, '0) max:', max(x), ', rms: ', rms(x), ' larm: ', larm(x), ' leq: ', leq(x), ' loudness: ', loudness(x)
	norm = giveNormalizer(x[:])
	print "norm: ", norm
	x = x * norm
	print file, '1) max:', max(x), ', rms: ', rms(x), ' larm: ', larm(x), ' leq: ', leq(x), ' loudness: ', loudness(x)
	writer = essentia.standard.MonoWriter(filename=join('eq', file))
	writer(x)












