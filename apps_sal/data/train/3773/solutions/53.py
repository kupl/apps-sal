def isValid(formula):
    if 7 in formula or 8 in formula:
        if not (1 in formula and 2 in formula):
            if not (3 in formula and 4 in formula):
                if 5 not in formula and (not 6 in formula) or (5 in formula and 6 in formula):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
