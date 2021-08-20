def weight(n, w):
    i0 = 0.14849853757254
    eConst = 2.71828182845904
    eInvConstSq = 1 / eConst ** 2
    nPartialWeight = 0
    nPartialSurface = i0
    for iArch in range(1, n + 1):
        nPartialWeight = nPartialWeight + iArch * nPartialSurface * w * (1 - eInvConstSq)
        nPartialSurface = nPartialSurface / eConst ** 2
    return nPartialWeight
