def isValid(formula):
    if 1 in formula and 2 in formula:
        return False
    elif 3 in formula and 4 in formula:
        return False
    elif 7 not in formula and 8 not in formula:
        return False
    elif 5 in formula:
        if not 6 in formula:
            return False
    elif 6 in formula:
        if not 5 in formula:
            return False
    return True
