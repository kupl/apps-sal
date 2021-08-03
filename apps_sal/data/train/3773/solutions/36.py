def isValid(formula):
    f = set(formula)
    if 7 not in f and 8 not in f:
        return False
    if 1 in f and 2 in f:
        return False
    if 3 in f and 4 in f:
        return False
    return (5 in f) == (6 in f)
