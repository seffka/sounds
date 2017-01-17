import random
import os
from os import listdir
from os.path import isfile, join, splitext

f = [f for f in listdir('.') if isfile(join('.', f)) and splitext(join('.', f))[1] == '.wav' and 'intro.wav' not in f]
res = []
confusions = {}
allFiles = {}
for line in f:
    parts = splitext(line)[0].split('_')
    instrument = parts[0]
    ad = parts[1]
    length = parts[2]
    other = parts[3]
    id = instrument + '_' + ad + '_' + length
    if (id in allFiles):
        allFiles[id].append(line)
    else:
        allFiles[id]=[line]

#allInstruments = ['piano', 'guitar', 'tambura', 'harpsichord']

for id in allFiles.keys():
    parts = id.split('_')
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
    falseFiles = []
    for falseInstrument in allInstruments:
        falseInstrumentId = falseInstrument + '_' + ad + '_' + length
        sh = allFiles[falseInstrumentId][:]
        random.shuffle(sh)
        falseFiles.extend(sh[:2])

    res.append([instrument, ' '.join(allFiles[id])])
    res.append([instrument, ' '.join(falseFiles)])

random.shuffle(res)

q = open('quiz.txt', 'w')
for x in res:
    q.write(x[0] + ' ' + x[1] + '\n');

q.close()