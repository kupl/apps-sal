def isValid(f):
    if 1 in f and 2 in f:
        return False
    if 3 in f and 4 in f:
        return False
    if not 7 in f and not 8 in f:
        return False
    if 5 in f and not 6 in f:
        return False
    if not 5 in f and 6 in f:
        return False
    return True
