def isValid(formula):
    if 7 in formula or 8 in formula:
        if 1 in formula and 2 in formula:
            return False
        elif 3 in formula and 4 in formula:
            return False
        elif 5 in formula:
            if 6 in formula:
                return True
            else:
                return False
        elif 6 in formula:
            if 5 in formula:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
