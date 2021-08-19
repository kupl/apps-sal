def isValid(formula):
    if 1 in formula and 2 in formula:
        print('1')
        return False
    elif 3 in formula and 4 in formula:
        print('2')
        return False
    elif 5 in formula and 6 not in formula:
        print('3')
        return False
    elif 6 in formula and 5 not in formula:
        print('4')
        return False
    elif not (7 in formula or 8 in formula):
        print('5')
        return False
    return True
