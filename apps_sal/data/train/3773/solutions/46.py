def isValid(formula):
    var1 = 7 in formula or 8 in formula
    if var1 == False:
        return False
    if 1 in formula and 2 in formula:
        return False
    if 3 in formula and 4 in formula:
        return False
    if 5 in formula:
        if 6 in formula:
            var1 = True
        else:
            return False
    if 6 in formula:
        if 5 in formula:
            var1 = True
        else:
            return False
    return True
