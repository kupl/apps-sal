def find_short(s):
    sList = s.split()
    shortestLength = len(sList[0])
    for item in sList:
        if len(item) < shortestLength:
            shortestLength = len(item)
    return shortestLength
