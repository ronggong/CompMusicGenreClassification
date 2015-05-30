import urllib, json

def dumpFeaturesIntoJson(recordingID, jsonOutputFolder, genre):
    url = 'http://acousticbrainz.org/' + recordingID + '/low-level'
    response = urllib.urlopen(url).read()
    try:
        lowlevel = json.loads(response)
        outputFilename = jsonOutputFolder + '/' + genre +'/' + recordingID +'.json'
    
        with open(outputFilename, 'w+') as outfile:
            json.dump(lowlevel, outfile)
            
        return True
    except:
        return False
    
    #print lowlevel