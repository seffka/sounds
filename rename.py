import random
import os
from os import listdir
from os.path import isfile, join, splitext

f = [f for f in listdir('.') if isfile(join('.', f)) and splitext(join('.', f))[1] == '.wav' and 'intro.wav' not in f]
res = []
confusions = {}
for line in f:
    # harpsichord_b4_noatck_32ms.wav -> {guitar|piano|tambura|harpsichord}_{a|d}_NNN_{pitch or whatever}.wav
    parts = splitext(line)[0].split('_')
    instrument = parts[0]
    pitch = parts[1]
    ad = parts[2]
    length = parts[3].strip('ms')
    if (ad == 'atck'):
        ad = 'a'
    else:
        ad = 'd'
    os.rename(line, instrument + '_' + ad + '_' + length + '_' + pitch + '.wav')

