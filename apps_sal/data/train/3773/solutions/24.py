def isValid(formula):
    test1 = not (1 in formula and 2 in formula)
    test2 = not (3 in formula and 4 in formula)
    test3 = 5 in formula and 6 in formula or (5 not in formula and 6 not in formula)
    test4 = 7 in formula or 8 in formula
    print((test1, test2, test3, test4))
    return test1 and test2 and test3 and test4
