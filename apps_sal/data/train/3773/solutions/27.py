def isValid(formula):
    list = []
    for x in range(8):
        list.append(9)
    for x in formula:
        list[x - 1] = x
    if((list[0] != 9) and (list[1] != 9)):
        return False
    elif((list[2] != 9) and (list[3] != 9)):
        return False
    elif((list[4] == 9 and list[5] != 9) or (list[4] != 9 and list[5] == 9)):
        return False
    elif((list[6] + list[7]) == 18):
        return False
    else:
        return True
