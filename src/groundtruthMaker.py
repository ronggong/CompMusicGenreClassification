def groundtruthMaker(className, groundtruthDict):
    rDict = {}
    rDict['className'] = className
    rDict['groundTruth'] = groundtruthDict
    rDict['type'] = 'singleClass'
    rDict['version'] = 1.0
    #rStr = 'className: ' + className + '\n' + groundtruthStr + '\n' + 'type: singleClass' + '\n' + 'version: 1.0'
    return rDict