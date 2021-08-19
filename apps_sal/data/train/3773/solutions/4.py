def isValid(formula):
    f = set(formula)
    return not {1, 2} <= f and (not {3, 4} <= f) and ((5 in f) == (6 in f)) and bool({7, 8} & f)
