def stringy(size):
    outStr = ''
    lastAdd = 0
    for x in range(size):
        if lastAdd == 0:
            outStr += str(1)
            lastAdd = 1
        else:
            outStr += str(0)
            lastAdd = 0
    return outStr
