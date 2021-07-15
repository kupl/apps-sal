def between(a,b):
    if (a < 0) and (b < 0):
        spis = [(min(a,b) + i) for i in range(b - a + 1)]
        return spis
    elif (b < 0):
        spis = [(min(a,b) + i) for i in range(abs(a) + abs(b) + 1)] 
        return spis
    elif (a < 0):
        spis = [(min(a,b) + i) for i in range(abs(a) + abs(b) + 1)] 
        return spis
    spis = [min(a,b) + i for i in range(b - a + 1)] 
    return spis

