import os, sys
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import featureReader as fReader

carnaticPath = '/Users/gong/Documents/MTG document/features/Carnatic'
hindustaniPath = '/Users/gong/Documents/MTG document/features/Hindustani'
jingjuPath = '/Users/gong/Documents/MTG document/features/Jingju'
makamPath = '/Users/gong/Documents/MTG document/features/Makam'

paths = [carnaticPath, hindustaniPath, jingjuPath, makamPath]

filenames = [ f for f in listdir(jingjuPath) if isfile(join(jingjuPath,f)) and f.endswith('.json') ]
jingjuLen = len(filenames)

featureArrays = [] # feature Array contains beats_loudness, dissonance, tuning_diatonic, tuning_equal_tempered
for ii in range(len(paths)):
    featureDict = {}
    bl = []
    ds = []
    td = []
    te = []
    jj = 1

    filenames = [ f for f in listdir(paths[ii]) if isfile(join(paths[ii],f)) and f.endswith('.json') ]
    fileAmount = len(filenames)

    for filename in filenames:
        filename = join(paths[ii], filename)
        beats_loudness, dissonance, tuning_diatonic, tuning_equal = fReader.readThem2List(filename)
        if beats_loudness <= 0.1: # for ploting , only get beats_loudness value <= 0.1
            bl.append(beats_loudness)
            
        ds.append(dissonance)
        td.append(tuning_diatonic)
        te.append(tuning_equal)
        
        #if jj >= jingjuLen:
        #    break
        jj += 1
    
    featureDict['bl'] = bl
    featureDict['ds'] = ds
    featureDict['td'] = td
    featureDict['te'] = te
    
    featureArrays.append(featureDict)
    
genres = ['Carnatic', 'Hindustani', 'Jingju', 'Makam']
colors = ['b', 'y', 'r', 'k']
features = ['bl', 'ds', 'td', 'te']
featuresName = ['beats loudness', 'dissonance', 'tuning diatonic', 'tuning equal tempered']

for jj in range(len(features)):
    fig, ax = plt.subplots()
    for ii in range(len(genres)):
        weights = np.ones_like(featureArrays[ii][features[jj]])/len(featureArrays[ii][features[jj]])
        plt.hist(featureArrays[ii][features[jj]], bins = 100, weights = weights, color= colors[ii], alpha=0.5, label=genres[ii])
        #plt.hist(featureArrays[ii][features[jj]], bins = 100, color= colors[ii], alpha=0.5, label=genres[ii])

    plt.title(featuresName[jj])
    plt.xlabel("feature value")
    plt.ylabel("amplitude")
    plt.legend(loc = 'best')
    plt.show()
