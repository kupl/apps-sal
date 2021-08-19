def is_keith_number(n):
    numList = [int(i) for i in str(n)]
    if len(numList) > 1:
        itr = 0
        while numList[0] <= n:
            numList[itr % len(numList)] = sum(numList)
            itr += 1
            if n in numList:
                return itr
    return False
