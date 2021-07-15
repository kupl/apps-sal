def isValid(formula: list) -> bool:
    if 7 in formula or 8 in formula or set([7, 8]).issubset(formula):
        if set([1, 2]).issubset(formula):
            return False
        if set([3, 4]).issubset(formula):
            return False
        if 5 in formula or 6 in formula:
            return set([5, 6]).issubset(formula)
        if 7 in formula or 8 in formula or set([7, 8]).issubset(formula):
            return True
    return False

