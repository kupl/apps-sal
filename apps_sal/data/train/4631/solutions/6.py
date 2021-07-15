def createDict(keys, values):
    """
    Write your code here.
    """
    newdict = {}
    for i in range(len(keys)):
        if i < len(values):
            newdict[keys[i]] = values[i]
        else:
            newdict[keys[i]] = None
    return newdict 
