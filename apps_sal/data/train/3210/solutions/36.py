def get_strings(inputString):
    checkDict = {
        "letter": [],
        "count": []
    }
    charArray = list(inputString.lower())
    for i in charArray:
        if i in checkDict['letter']:
            k = checkDict['letter'].index(i)
            checkDict['count'][k] = checkDict['count'][k] + '*'
        else:
            if (i.isalpha()):
                checkDict['letter'].append(i)
                checkDict['count'].append('*')
    outputString = ''
    for i in checkDict['letter']:
        indexLetter = checkDict['letter'].index(i)
        outputString = outputString + i + ':' + checkDict['count'][indexLetter] + ','
    return outputString[:-1]
