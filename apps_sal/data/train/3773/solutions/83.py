def isValid(f):
    if len(f) == 1 and f[0] != 7 and f[0] != 8:
        return False
    elif 1 in f and 2 in f:
        return False
    elif 3 in f and 4 in f:
        return False
    elif 5 not in f and 6 in f:
        return False
    elif 5 in f and 6 not in f:
        return False
    elif 7 in f or 8 in f:
        return True
    else:
        return False
