def isValid(f):
    return ((1 not in f) or (2 not in f)) and \
        ((3 not in f) or (4 not in f)) and \
        ((5 in f) == (6 in f)) and \
        ((7 in f) or (8 in f))
