def isValid(formula):
    print(formula)
    if 1 in formula and 2 in formula:
        return 0
    if 3 in formula and 4 in formula:
        return 0
    if 5 in formula and not 6 in formula:
        return 0
    if 6 in formula and not 5 in formula:
        return 0
    if 7 in formula or 8 in formula:
        return 1
    else:
        return 0
