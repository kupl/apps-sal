def isValid(formula):
    if len(set(formula).intersection(set([1, 2]))) > 1 or len(set(formula).intersection(set([3, 4]))) > 1 or len(set(formula).intersection(set([5, 6]))) == 1 or len(set(formula).intersection(set([7, 8]))) < 1:
        return False
    return True
