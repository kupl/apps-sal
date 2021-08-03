def isValid(formula):
    if 1 in formula and 2 in formula:
        return False
    if 3 in formula and 4 in formula:
        return False
    if 5 in formula and 6 not in formula:
        return False
    if not 5 in formula and 6 in formula:
        return False
    if not 7 in formula and not 8 in formula:
        return False
    return True
