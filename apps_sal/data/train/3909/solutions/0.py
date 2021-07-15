def is_keith_number(n):
    numList = [int(i) for i in str(n)]  # int array
    if len(numList) > 1:  # min 2 digits
        itr = 0
        while numList[0] <= n:
            # replace array entries by its sum:
            numList[itr % len(numList)] = sum(numList)
            itr += 1
            if n in numList:  # keith-condition
                return itr
    return False
