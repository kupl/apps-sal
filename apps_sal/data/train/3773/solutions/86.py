def isValid(formula):
    if len(formula) == 0:
        return False
    elif len(formula) == 1:
        if 7 in formula or 8 in formula:
            return True
        else:
            return False
    elif len(formula) == 2:
        if 7 in formula and 8 in formula:
            return True
        elif 7 in formula or 8 in formula:
            if 5 in formula or 6 in formula:
                return False
            else:
                return True
        else:
            return False
    elif len(formula) == 3:
        if 7 in formula and 8 in formula:
            if 5 in formula or 6 in formula:
                return False
            else:
                return True
        elif 7 in formula or 8 in formula:
            if 5 in formula and 6 in formula:
                return True
            elif 3 in formula and 4 not in formula or (4 in formula and 3 not in formula):
                if 1 in formula and 2 not in formula or (2 in formula and 1 not in formula):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif len(formula) == 4:
        if 7 in formula and 8 in formula:
            if 5 in formula and 6 in formula:
                return True
            elif 3 in formula and 4 not in formula or (4 in formula and 3 not in formula):
                if 1 in formula and 2 not in formula or (2 in formula and 1 not in formula):
                    return True
                else:
                    return False
            else:
                return False
        elif 7 in formula or 8 in formula:
            if 5 in formula and 6 in formula:
                return True
            else:
                return False
        else:
            return False
    elif len(formula) == 5:
        if 7 in formula and 8 in formula:
            if 5 in formula and 6 in formula:
                return True
            else:
                return False
        elif 7 in formula or 8 in formula:
            if 5 in formula and 6 in formula:
                if 3 in formula and 4 not in formula or (4 in formula and 3 not in formula):
                    if 1 in formula and 2 not in formula or (2 in formula and 1 not in formula):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif len(formula) == 6:
        if 7 in formula and 8 in formula:
            if 5 in formula and 6 in formula:
                if 3 in formula and 4 not in formula or (4 in formula and 3 not in formula):
                    if 1 in formula and 2 not in formula or (2 in formula and 1 not in formula):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif len(formula) > 6:
        return False
