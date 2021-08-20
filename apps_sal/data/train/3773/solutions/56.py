def isValid(formula):
    return not any([1 in formula and 2 in formula, 3 in formula and 4 in formula, 5 in formula and (not 6 in formula), 6 in formula and (not 5 in formula)]) and any([7 in formula, 8 in formula])
