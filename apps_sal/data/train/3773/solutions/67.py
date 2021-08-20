def isValid(formula):
    count_1 = formula.count(1)
    count_2 = formula.count(2)
    if count_1 == count_2 == 1:
        return False
    count_1 = formula.count(3)
    count_2 = formula.count(4)
    if count_1 == count_2 == 1:
        return False
    count_1 = formula.count(5)
    count_2 = formula.count(6)
    if count_1 != count_2:
        return False
    count_1 = formula.count(7)
    count_2 = formula.count(8)
    if count_1 == count_2 == 0:
        return False
    return True
