def tidyNumber(n):
    numLst = list(str(n))
    for i in range(len(numLst) - 1):
        if not numLst[i + 1] >= numLst[i]:
            return False
    return True
