from itertools import cycle

def sumDig_nthTerm(initVal, patternL, nthTerm):
    
    for c, i in enumerate(cycle(patternL), 2):
        initVal += i
        
        if c == nthTerm:
            return sum(int(v) for v in str(initVal))
