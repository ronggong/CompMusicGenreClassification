import json

def beats_loudness(featureDict):
    return featureDict['rhythm']['beats_loudness']['median']
    
def dissonance(featureDict):
    return featureDict['lowlevel']['dissonance']['median']

def tuning_diatonic(featureDict):
    return featureDict['tonal']['tuning_diatonic_strength']

def tuning_equal_tempered(featureDict):
    return featureDict['tonal']['tuning_equal_tempered_deviation']
    
def readThem2List(jsonPath):
    with open(jsonPath) as data_file:    
        data = json.load(data_file)
    
        bl = beats_loudness(data)
        ds = dissonance(data)
        td = tuning_diatonic(data)
        te = tuning_equal_tempered(data)
    
    return bl, ds, td, te