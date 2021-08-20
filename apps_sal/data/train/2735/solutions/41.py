def jumping_number(number):
    numLst = [int(x) for x in str(number)]
    for i in range(len(numLst) - 1):
        if not abs(numLst[i] - numLst[i + 1]) == 1:
            return 'Not!!'
    return 'Jumping!!'
