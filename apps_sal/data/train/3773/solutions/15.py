def isValid(f):
    return ((1 in f) ^ (2 in f) or (1 not in f and 2 not in f)) and ((3 in f) ^ (4 in f) or (3 not in f and 4 not in f)) and (5 in f and 6 in f or (5 not in f and 6 not in f)) and ((7 in f) | (8 in f))
