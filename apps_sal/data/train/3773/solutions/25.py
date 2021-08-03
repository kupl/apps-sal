def isValid(formula):
    if 3 in formula and 4 in formula:
        return False
    elif 1 in formula and 2 in formula:
        return False
    elif 5 in formula and 6 not in formula:
        return False
    elif 5 not in formula and 6 in formula:
        return False
    elif 7 not in formula and 8 not in formula:
        return False
    else:
        return True
