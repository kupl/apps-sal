def isValid(formula):
    return (1 in formula) + (2 in formula) < 2 and (3 in formula) + (4 in formula) < 2 and ((5 in formula) == (6 in formula)) and (7 in formula or 8 in formula)
