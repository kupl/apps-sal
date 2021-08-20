def sumDig_nthTerm(initVal, patternL, nthTerm):
    (q, r) = divmod(nthTerm - 1, len(patternL))
    x = initVal + q * sum(patternL) + sum(patternL[:r])
    return sum(map(int, str(x)))
