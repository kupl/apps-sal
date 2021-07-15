def isValid(f):
    return ((7 in f) or (8 in f)) and not(((5 in f) and (6 not in f)) or ((6 in f) and (5 not in f))) and not ((1 in f) and (2 in f)) and not ((3 in f) and (4 in f))
