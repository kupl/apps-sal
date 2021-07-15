def shortest_arrang(n):
    nGrpMax = int( ((1+8*n)**.5-1)/2 )
    for nGrp in range(2, nGrpMax+1):
        maxInG = (2*n + nGrp**2 - nGrp) / (2*nGrp)
        if maxInG == int(maxInG):
            maxInG = int(maxInG)
            return list(range(maxInG, maxInG-nGrp, -1))
    return [-1]
