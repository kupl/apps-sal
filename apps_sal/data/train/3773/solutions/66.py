def isValid(f):
    if 7 not in f and 8 not in f:
        return False
    if 1 in f and 2 in f:
        return False
    if 3 in f and 4 in f:
        return False
    if 5 in f and 6 not in f:
        return False
    if 6 in f and 5 not in f:
        return False
    return True
