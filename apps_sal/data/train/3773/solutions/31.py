def isValid(f):
    return all((7 in f or 8 in f, (5 in f) == (6 in f), not (3 in f and 4 in f), not (1 in f and 2 in f)))
