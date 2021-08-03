def isValid(formula):
    if formula.count(1) and formula.count(2):
        return False
    if formula.count(3) and formula.count(4):
        return False
    if formula.count(5) + formula.count(6) == 1:
        return False
    if formula.count(7) + formula.count(8) == 0:
        return False
    return True
