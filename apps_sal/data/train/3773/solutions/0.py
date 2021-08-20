def isValid(formula):
    return not (1 in formula and 2 in formula or (3 in formula and 4 in formula) or (5 in formula and (not 6 in formula)) or (not 5 in formula and 6 in formula) or (not 7 in formula and (not 8 in formula)))
