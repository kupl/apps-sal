def isValid(formula):
    rules = list()
    rules.append(1) if 7 in formula or 8 in formula else rules.append(0)
    if 5 in formula or 6 in formula:
        rules.append(2) if 5 in formula and 6 in formula else rules.append(0)
    if 3 in formula or 4 in formula:
        rules.append(0) if 3 in formula and 4 in formula else rules.append(3)
    if 1 in formula or 2 in formula:
        rules.append(0) if 1 in formula and 2 in formula else rules.append(4)
    return True if min(rules) != 0 else False
