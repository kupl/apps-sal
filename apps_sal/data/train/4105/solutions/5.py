def sumDig_nthTerm(initVal, patternL, nthTerm):
    n = initVal
    for i in range(nthTerm - 1):
        n += patternL[i % len(patternL)]
    return sum((int(d) for d in str(n)))
