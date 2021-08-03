def two_highest(arg1):
    if arg1 == []:
        return arg1
    returnArr = []
    val1 = max(arg1)
    returnArr.append(val1)
    for i in range(len(arg1)):
        if val1 in arg1:
            arg1.remove(val1)
    if arg1 == []:
        return returnArr
    val2 = max(arg1)
    if val2 == None:
        return returnArr
    returnArr.append(val2)
    return returnArr
