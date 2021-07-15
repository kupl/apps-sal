def isValid(formula): 
    if 1 in formula and 2 in formula: return False
    elif 3 in formula and 4 in formula: return False
    elif 5 in formula and 6 not in formula: return False
    elif 6 in formula and 5 not in formula: return False
    elif 7 in formula or 8 in formula: return True
    elif 7 not in formula or 8 not in formula: return False

