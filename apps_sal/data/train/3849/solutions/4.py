def spacify(string):
    retVal = ""
    for ch in string:
        retVal += ch + " "

    return retVal[:-1]
