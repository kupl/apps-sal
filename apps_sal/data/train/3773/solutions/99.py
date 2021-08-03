def isValid(formula):

    return ((7 in formula or 8 in formula) and not(1 in formula and 2 in formula) and not(3 in formula and 4 in formula) and ((5 in formula and 6 in formula) or (5 not in formula and 6 not in formula)))
