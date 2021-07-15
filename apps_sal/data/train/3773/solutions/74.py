def isValid(formula):
    flag = True
    if 1 in formula:
        if 2 in formula:
            flag = False
    if 3 in formula:
        if 4 in formula:
            flag = False
    if 5 in formula:
        if 6 not in formula:
            flag = False
    if 6 in formula:
        if 5 not in formula:
            flag = False
    if 7 not in formula and 8 not in formula:
        flag = False
    return flag
