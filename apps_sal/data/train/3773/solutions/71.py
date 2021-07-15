def isValid(formula):
    # material7 or  material8 must be selected(at least one, or both)
    if 7 in formula or 8 in formula:
    # material5 and material6 must be selected at the same time
        if (5 in formula and 6 in formula) or (not 5 in formula and not 6 in formula):
    # material3 and material4 cannot be selected at the same time
            if (3 in formula and not 4 in formula) or (4 in formula and not 3 in formula) or (not 3 in formula and not 4 in formula):
    # material1 and material2 cannot be selected at the same time
                if (1 in formula and not 2 in formula) or (2 in formula and not 1 in formula) or (not 1 in formula and not 2 in formula):
                    return True
                else: return False
            else: return False
        else: return False
    else: return False
