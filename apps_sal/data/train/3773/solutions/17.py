def isValid(f):
    invalid = ((1, 2), (3, 4))
    if 1 in f and 2 in f:
        return False
    if 3 in f and 4 in f:
        return False
    if (5 in f or 6 in f) and (not (5 in f and 6 in f)):
        return False
    if not (7 in f or 8 in f):
        return False
    return True
