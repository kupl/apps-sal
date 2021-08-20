def isValid(formula):
    if 7 in formula or 8 in formula:
        if 5 in formula and 6 in formula or (not 5 in formula and (not 6 in formula)):
            if 3 in formula and (not 4 in formula) or (4 in formula and (not 3 in formula)) or (not 3 in formula and (not 4 in formula)):
                if 1 in formula and (not 2 in formula) or (2 in formula and (not 1 in formula)) or (not 1 in formula and (not 2 in formula)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
