import itertools


def getAllCombinations(numStr, numDigits):
    combedDigits = []
    for d in range(1, numDigits + 1):
        numList = [(''.join(p)) for p in itertools.combinations(numStr, d)]
        uniqueNumList = set(numList)
        combedDigits.append(uniqueNumList)

    return combedDigits


def sc_perm_comb(n):
    numStr = str(n)
    numDigits = len(numStr)

    combStrList = getAllCombinations(numStr, numDigits)

    permSet = set()
    for numsOfDigitD in combStrList:
        for num in numsOfDigitD:
            allPerms = [int(''.join(p)) for p in itertools.permutations((num)) if p[0] != '0']
            permSet.update(set(allPerms))

    totalSum = sum(permSet)

    return totalSum
