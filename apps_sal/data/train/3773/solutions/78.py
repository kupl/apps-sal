def isValid(formula):
    """
        Returns true if the formula is valid, false otherwise.
        
        Rules:
        • material1 and material2 cannot be selected at the same time
        • material3 and material4 cannot be selected at the same time
        • material5 and material6 must be selected at the same time
        • material7 or  material8 must be selected(at least one, or both)
    """
    if 1 in formula and 2 in formula:
        return False
    
    if 3 in formula and 4 in formula:
        return False
    
    if 5 in formula or 6 in formula:
        if 5 not in formula or 6 not in formula:
            return False
    
    if 7 not in formula and 8 not in formula:
        return False
    
    return True
