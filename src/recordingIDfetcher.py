import compmusic as cm
from compmusic import dunya as dy

dy.conn.set_token('0186a989507de593d7e83e530a7a5c1280507217')

def carnaticRecordingIDfetcher():
    '''this function get all recordingIDs for all carnatic artistis
    no need to query concerts for the recording IDs, because the carnatic
    api is well developped.'''
    # get artists
    carnaticArtists = dy.carnatic.get_artists()
    
    # get artist mbids
    carnaticMBIDs = []
    for carnaticArtist in carnaticArtists:
        carnaticMBIDs.append(carnaticArtist['mbid'])
        
    # get recordingID
    carnaticRecordingIDs = []
    ii = 1
    length = len(carnaticMBIDs)
    
    print 'fetching carnatic recording Ids... ...'
    for mbid in carnaticMBIDs:
        rdic = dy.carnatic.get_artist(mbid)
        rdic = rdic['recordings']
        
        if len(rdic) != 0:
            for recording in rdic:
                carnaticRecordingIDs.append(recording['mbid'])
        
        print 'fetching carnatic artist number ', ii, 'of total ', length
        ii += 1
        
    return carnaticRecordingIDs

def hindustaniRecordingIDfetcher():
    '''this function get all recordingIDs for all hindustani artistis
    no need to query releases for the recording IDs, because the hindustani
    api is well developped.'''
    # get artists
    hindustaniArtists = dy.hindustani.get_artists()
    
    # get artist mbids
    hindustaniMBIDs = []
    for hindustaniArtist in hindustaniArtists:
        hindustaniMBIDs.append(hindustaniArtist['mbid'])
                
    # get recordingID
    hindustaniRecordingIDs = []
    ii = 1
    length = len(hindustaniMBIDs)
    
    print 'fetching hindustani recording Ids... ...'
    for mbid in hindustaniMBIDs:
        rdic = dy.hindustani.get_artist(mbid)
        rdic = rdic['recordings']
        
        if len(rdic) != 0:
            for recording in rdic:
                hindustaniRecordingIDs.append(recording['mbid'])
        
        print 'fetching hindustani artist number ', ii, 'of total ', length
        # if ii/float(length) > jj/20:
#             print 'fetched ', jj, '/', 20
#             jj += 1
        ii += 1
    return hindustaniRecordingIDs
    
def makamRecordingIDfetcher():
    '''this function get all recordingIDs for all markam artistis
    we need to query releases firstly'''
    # get artists
    makamArtists = dy.makam.get_artists()
    
    # get artist mbids
    makamMBIDs = []
    for makamArtist in makamArtists:
        makamMBIDs.append(makamArtist['mbid'])
        
    # get recordingID
    makamRecordingIDs = []
    ii = 1
    length = len(makamMBIDs)
    
    print 'fetching makam recording Ids... ...'
    for mbid in makamMBIDs:
        rdic = dy.makam.get_artist(mbid)
        # print rdic
        
        if 'releases' in rdic:
            rdic = rdic['releases'] # release of the artist
            
            if len(rdic) != 0:
                for release in rdic:                    
                    releaseDict = dy.makam.get_release(release['mbid'])
                    recordingArray = releaseDict['recordings'] # recordings of the release
                    if len(recordingArray) != 0:
                        for recording in recordingArray:
                            makamRecordingIDs.append(recording['mbid'])
        
        print 'fetching markam artist number ', ii, 'of total ', length
        ii += 1
    return makamRecordingIDs
    
    