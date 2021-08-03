def isValid(formula):
    formula = sorted(formula)
    if len(formula) < 1:
        return False
    elif (1 in formula and 2 in formula) or (3 in formula and 4 in formula) or (7 not in formula and 8 not in formula):
        return False
    elif (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        return False
    else:
        return True
