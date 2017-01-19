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

def processLength(l, x, instrument, pitch):
    s = int(44100 * l / 1000.0)
    _8ms = int(44100 * .008)
    aw = np.ones(s)
    dw = np.ones(s)
    hw = get_window('hamming', _8ms)
    dw[:_8ms / 2] = hw[:_8ms / 2]
    dw[-_8ms / 2:] = hw[-_8ms / 2:]
    aw[-_8ms / 2:] = hw[-_8ms / 2:]
    ax = x[:s] * aw
    dx = x[int(44100 * 0.08): int(44100 * 0.08) + s] * dw
    file_a = instrument + '_a_' + str(l) + '_' + pitch + '.wav'
    file_d = instrument + '_d_' + str(l) + '_' + pitch + '.wav'
    writer = essentia.standard.MonoWriter(filename=join('hacked', file_a))
    writer(ax.astype(np.float32))
    writer = essentia.standard.MonoWriter(filename=join('hacked', file_d))
    writer(dx.astype(np.float32))

f = [f for f in listdir('raw') if isfile(join('raw', f)) and splitext(join('.', f))[1] == '.wav' and 'intro.wav' not in f]
for file in f:
    loader = essentia.standard.MonoLoader(filename=join('raw', file))
    x = loader()
    parts = splitext(file)[0].split('_')
    instrument = parts[0]
    pitch = parts[1]
    processLength(16, x, instrument, pitch)
    processLength(24, x, instrument, pitch)
    processLength(32, x, instrument, pitch)
    processLength(64, x, instrument, pitch)
    processLength(128, x, instrument, pitch)
    processLength(500, x, instrument, pitch)





