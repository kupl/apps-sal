def isValid(formula):
    if 1 in formula and 2 in formula:
        return False
    if 3 in formula and 4 in formula:
        return False
    if (6 in formula) != (5 in formula):
        return False
    if not 7 in formula and (not 8 in formula):
        return False
    return True
