def two_sort(array):
    firstElem = sorted(array)[0]
    returnArr = [] 
    for i in range(len(firstElem)-1): 
        returnArr.append(firstElem[i])
        returnArr.append('***')
    returnArr.append(firstElem[-1])
    return "".join(returnArr)
