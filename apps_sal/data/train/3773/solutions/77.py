def isValid(formula):
    if 7 in formula or 8 in formula:
        if 1 in formula and 2 in formula or (3 in formula and 4 in formula):
            return False
        if 5 in formula and 6 not in formula or (6 in formula and 5 not in formula):
            return False
        return True
    return False
