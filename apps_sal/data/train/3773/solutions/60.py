def isValid(formula):
    r1 = not (1 in formula and 2 in formula)
    r2 = not (3 in formula and 4 in formula)
    r3 = (5 in formula) == (6 in formula)
    r4 = 7 in formula or 8 in formula
    return all([r1, r2, r3, r4])
