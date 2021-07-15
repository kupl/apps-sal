def isValid(formula):
    if 7 in formula or 8 in formula:
        if 1 in formula and 2 in formula:
            return False
        if 3 in formula and 4 in formula:
            return False
        if (5 in formula and not 6 in formula) or (6 in formula and not 5 in formula):
            return False
        return True
    else:
        return False

