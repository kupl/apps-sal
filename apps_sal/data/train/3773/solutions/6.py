def isValid(formula):
    if {1,2} <= set(formula) or {3,4} <= set(formula):
        print(1)
        return False
    elif (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        print(3)
        return False
    elif 7 not in formula and 8 not in formula:
        print(4)
        return False
    else:
        return True
