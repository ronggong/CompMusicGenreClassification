# -*- coding: utf-8 -*-

import os, sys
sys.path.append('/Users/gong/Documents/Library/gaia-master/src/bindings/pygaia/scripts/classification')
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import recordingIDfetcher as fetcher
import jingjuRecordingIDreader as reader
import dumpFeaturesIntoJson as jsonDumper
import convertJsonToSig as j2s
import groundtruthMaker as gtMaker
import urllib, json, yaml
import train_model as tm

# ----- folders
outputFolder = "/Users/gong/Documents/MTG document/features"
jingjuFolder = "/Users/gong/Documents/MTG document/Jingju arias/京剧之星"

# ----- fetch carnatic, hindustani and makam recordingIDs
carnaticRecordingIDs = fetcher.carnaticRecordingIDfetcher()
hindustaniRecordingIDs = fetcher.hindustaniRecordingIDfetcher()
makamRecordingIDs = fetcher.makamRecordingIDfetcher()

# ----- read jingju recordingIds
jingjuRecordingIDs = reader.jingjuRecordingIDreader(jingjuFolder)

# ----- filelist and groundtruth dictionaries
filelistJson = {}
filelistYaml = {}
groundtruthDict = {}

# ----- write groundtruth and filelist
ii = 1
genre = 'Jingju'
lengthOfJingjuRecordingIDs = len(jingjuRecordingIDs)
for recordingID in jingjuRecordingIDs:
    # jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
    print 'dumping low level features ', ii, ' into json file of total ', lengthOfJingjuRecordingIDs 
    
    filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
    filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
    groundtruthDict[recordingID] = genre
    ii += 1


ii = 1
jj = 1 # dumping sucessfully index
loopedRecordingIDs = [] # for 
genre = 'Carnatic'
length = len(carnaticRecordingIDs)
for recordingID in carnaticRecordingIDs:
    if recordingID not in loopedRecordingIDs:
        rFlag = jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
        if rFlag == True:
            print 'dumping low level features ', ii, ' into json file of total ', length 
            recordingID = recordingID.encode('ascii')
            filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
            filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
            groundtruthDict[recordingID] = genre
        
            if jj >= lengthOfJingjuRecordingIDs:
                print 'stop collecting carnatic music feature, we have the same amont of carnatic as ', lengthOfJingjuRecordingIDs
                break
            print 'successfully dumping ', jj, ' into json file' 
            jj += 1
        else:
            print 'dumping low level features ', ii, 'failed of total ', length
        
        loopedRecordingIDs.append(recordingID)
        ii += 1

ii = 1
jj = 1
genre = 'Hindustani'
loopedRecordingIDs = []
length = len(hindustaniRecordingIDs)
for recordingID in hindustaniRecordingIDs:
    if recordingID not in loopedRecordingIDs:
        rFlag = jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
        if rFlag == True:
            print 'dumping low level features ', ii, ' into json file of total ', length 
            recordingID = recordingID.encode('ascii')
            filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
            filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
            groundtruthDict[recordingID] = genre
        
            if jj >= lengthOfJingjuRecordingIDs:
                print 'stop collecting hindustani music feature, we have the same amont of hindustani music as ', lengthOfJingjuRecordingIDs
                break
            print 'successfully dumping ', jj, ' into json file' 
            jj += 1
        else:
            print 'dumping low level features ', ii, 'failed of total ', length
            
        loopedRecordingIDs.append(recordingID)
        ii += 1

ii = 1
jj = 1
genre = 'Makam'
loopedRecordingIDs = []
length = len(makamRecordingIDs)
for recordingID in makamRecordingIDs:
    if recordingID not in loopedRecordingIDs:
        rFlag = jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
        if rFlag == True and (recordingID not in loopedRecordingIDs):
            print 'dumping low level features ', ii, ' into json file of total ', length 
            recordingID = recordingID.encode('ascii')
            filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
            filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
            groundtruthDict[recordingID] = genre
        
            if jj >= lengthOfJingjuRecordingIDs:
                print 'stop collecting makam music feature, we have the same amont of makam music as ', lengthOfJingjuRecordingIDs
                break
            print 'successfully dumping ', jj, ' into json file' 
            jj += 1
        else:
            print 'dumping low level features ', ii, 'failed of total ', length
        
        loopedRecordingIDs.append(recordingID)
        ii += 1

# -----check the song amont of each genre
jingjuLen = 1
carnaticLen = 1
hindustaniLen = 1
makamLen = 1
for key, value in groundtruthDict.iteritems():
    if value == 'Jingju':
        jingjuLen += 1
    if value == 'Carnatic':
        carnaticLen += 1
    if value == 'Hindustani':
        hindustaniLen += 1
    if value == 'Makam':
        makamLen += 1

def amontCheck(genre, length, jingjuLen):
    if length != jingjuLen:
        print genre, length, ' is != ', jingjuLen
        return False
    else:
        print genre, length, ' is = ', jingjuLen
        return True
        
rFlag0 = amontCheck('Carnatic', carnaticLen, jingjuLen)
rFlag1 = amontCheck('Hindustani', hindustaniLen, jingjuLen)
rFlag2 = amontCheck('Makam', makamLen, jingjuLen)

if not rFlag0 or not rFlag1 or not rFlag2:
    print 'classification interrupted, because of non-equal amont of songs.'
    sys.exit()

# -----write groundtruth
groundtruth = gtMaker.groundtruthMaker('compMusicGenreClassification', groundtruthDict) # write ground

# -----dump filelist and groundtruth into yamls
filelistFilenameJson = outputFolder + '/filelistJson.yaml'	# json feature file list
filelistFilenameYaml = outputFolder + '/filelistYaml.yaml'  # yaml feature file list
groundtruthFilenameYaml = outputFolder + '/groundtruthYaml.yaml'

yaml.dump(filelistJson, open(filelistFilenameJson, 'w+'))
yaml.dump(filelistYaml, open(filelistFilenameYaml, 'w+'))
yaml.dump(groundtruth, open(groundtruthFilenameYaml, 'w+'))

print 'converting json filelist to yaml... ...'
j2s.convertJsonToSig(filelistFilenameJson, filelistFilenameYaml)

# -----training
print 'training model... ...'

project_dir = outputFolder + '/project_dir'
project_file = outputFolder + '/project_dir/project_file'
results_model_file = outputFolder + '/project_dir/results.history'

tm.trainModel(groundtruthFilenameYaml, filelistFilenameYaml, project_file, project_dir, results_model_file)




