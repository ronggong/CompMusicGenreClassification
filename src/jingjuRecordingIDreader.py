# -*- coding: utf-8 -*-

import compmusic as cm
import os
from os import listdir
from os.path import isfile, join

def jingjuRecordingIDreader(folder):
    mp3Files = []
    recordingIDs = []
    for name in listdir(folder):
        if not name.startswith('.'):
            name = "/Users/gong/Documents/MTG document/Jingju arias/京剧之星/" + name + '/'
            files = [ join(name, f) for f in listdir(name) if isfile(join(name,f)) and f.endswith('.mp3')]
            mp3Files = mp3Files + files

    ii = 1
    length = len(mp3Files)
    for f in mp3Files:
        recordingIDs.append(cm.file_metadata(f)['meta']['recordingid'])
        print 'reading recording ID ', ii, 'of total', length
        ii += 1
    
    return recordingIDs