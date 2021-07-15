def isValid(f):
    if 1 in f and 2 in f:
        return False
    elif 3 in f and 4 in f:
        return False
    elif (5 in f and not(6 in f)) or (6 in f and not(5 in f)):
        return False
    elif not(7 in f) and not(8 in f):
        return False
    return True
