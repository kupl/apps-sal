import itertools

#With combinations, we allow leading zeros, e.g. '03' is allowed, because when we permute, '03' becomes '30'  
def getAllCombinations(numStr, numDigits):
    combedDigits = []
    for d in range(1, numDigits+1):     #interval [1, numDigits]
        numList = [(''.join(p)) for p in itertools.combinations(numStr, d) ]
        uniqueNumList = set(numList)
        combedDigits.append( uniqueNumList )

    return combedDigits
#-----end function


def sc_perm_comb( n ):
    numStr = str(n)
    numDigits = len(numStr)

    combStrList = getAllCombinations(numStr, numDigits)

    permSet = set()
    for numsOfDigitD in combStrList:
        for num in numsOfDigitD:
            allPerms = [int(''.join(p)) for p in itertools.permutations((num)) if p[0]!='0']
            permSet.update(set(allPerms))    #punch out all repeats

    totalSum  = sum( permSet )

    return totalSum
#---end function

