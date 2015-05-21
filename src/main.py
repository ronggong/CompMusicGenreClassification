# -*- coding: utf-8 -*-

import recordingIDfetcher as fetcher
import jingjuRecordingIDreader as reader
import dumpFeaturesIntoJson as jsonDumper
import convertJsonToSig as j2s
import groundtruthMaker as gtMaker
import urllib, json, yaml, sys

sys.path.append('/Users/gong/Documents/Library/gaia-master/src/bindings/pygaia/scripts/classification')
import train_model as tm

# ----- main output folder
outputFolder = "/Users/gong/Documents/MTG document/features"

# ----- fetch carnatic, hindustani and makam recordingIDs
carnaticRecordingIDs = fetcher.carnaticRecordingIDfetcher()
hindustaniRecordingIDs = fetcher.hindustaniRecordingIDfetcher()
makamRecordingIDs = fetcher.makamRecordingIDfetcher()

# ----- read jingju recordingIds
jingjuFolder = "/Users/gong/Documents/MTG document/Jingju arias/京剧之星"
jingjuRecordingIDs = reader.jingjuRecordingIDreader(jingjuFolder)

# ----- filelist and groundtruth dictionaries
filelistJson = {}
filelistYaml = {}
groundtruthDict = {}

# ----- write groundtruth and filelist
ii = 1
genre = 'Jingju'
length = len(jingjuRecordingIDs)
for recordingID in jingjuRecordingIDs:
    # jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
    print 'dumping low level features ', ii, ' into json file of total ', length 
    
    filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
    filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
    groundtruthDict[recordingID] = genre
    ii += 1


ii = 1
genre = 'Carnatic'
length = len(carnaticRecordingIDs[:500])
for recordingID in carnaticRecordingIDs[:500]:
    rFlag = jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
    if rFlag == True:
        print 'dumping low level features ', ii, ' into json file of total ', length 
        recordingID = recordingID.encode('ascii')
        filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
        filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
        groundtruthDict[recordingID] = genre
    else:
        print 'dumping low level features ', ii, 'failed of total ', length
    ii += 1

ii = 1
genre = 'Hindustani'
length = len(hindustaniRecordingIDs[:500])
for recordingID in hindustaniRecordingIDs[:500]:
    rFlag = jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
    if rFlag == True:
        print 'dumping low level features ', ii, ' into json file of total ', length 
        recordingID = recordingID.encode('ascii')
        filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
        filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
        groundtruthDict[recordingID] = genre
    else:
        print 'dumping low level features ', ii, 'failed of total ', length
    ii += 1

ii = 1
genre = 'Makam'
length = len(makamRecordingIDs[:500])
for recordingID in makamRecordingIDs[:500]:
    rFlag = jsonDumper.dumpFeaturesIntoJson(recordingID, outputFolder, genre)
    if rFlag == True:
        print 'dumping low level features ', ii, ' into json file of total ', length 
        recordingID = recordingID.encode('ascii')
        filelistJson[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.json'
        filelistYaml[recordingID] = outputFolder + '/' + genre +'/' + recordingID +'.sig'
        groundtruthDict[recordingID] = genre
    else:
        print 'dumping low level features ', ii, 'failed of total ', length
    ii += 1

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




