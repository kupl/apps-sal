def isValid(formula):
    valid_formula = True

    if all(x in formula for x in [1, 2]):
        valid_formula = False

    if all(x in formula for x in [3, 4]):
        valid_formula = False

    if 5 in formula and 6 not in formula:
        valid_formula = False
        
    if 6 in formula and 5 not in formula:
        valid_formula = False
        
    if 7 not in formula and 8 not in formula:
        valid_formula = False



    return valid_formula
