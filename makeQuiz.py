import random
import os
from os import listdir
from os.path import isfile, join, splitext

f = [f for f in listdir('.') if isfile(join('.', f)) and splitext(join('.', f))[1] == '.wav' and 'intro.wav' not in f]
res = []
confusions = {}
for line in f:
    parts = splitext(line)[0].split('_')
    instrument = parts[0]
    ad = parts[1]
    length = parts[2]
    print instrument, ad, length
    allInstruments = set()

    allInstruments.add('piano')
    allInstruments.add('guitar')
    allInstruments.add('tambura')
    allInstruments.add('harpsichord')
    allInstruments.discard(instrument)
    restInstruments = list(allInstruments)
    falseInstrument = restInstruments[random.randint(0, len(allInstruments) - 2)]
    res.append([instrument, line])
    res.append([falseInstrument, line])
    confKey = instrument +':' + falseInstrument
    if (confusions.has_key(confKey)) :
        confusions[confKey] = confusions[confKey] + 1
    else:
        confusions[confKey] = 1

print 'confusions: ', confusions

random.shuffle(res)

q = open('quiz.txt', 'w')
for x in res:
    q.write(x[0] + ' ' + x[1] + '\n');

q.close()