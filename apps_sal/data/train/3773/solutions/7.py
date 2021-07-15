def isValid(formula):
    if not any(el in formula for el in (7, 8)):
        return False
    elif all(el in formula for el in (1, 2)):
        return False
    elif all(el in formula for el in (3, 4)):
        return False
    elif 5 in formula and 6 not in formula:
        return False
    elif 6 in formula and 5 not in formula:
        return False
    else:
        return True
