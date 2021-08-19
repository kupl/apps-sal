def isValid(formula):
    exclusive = [[1, 2], [3, 4]]
    implies = {5: 6, 6: 5}
    required = {7, 8}
    for (m1, m2) in exclusive:
        if m1 in formula and m2 in formula:
            return False
    for m in formula:
        if m in implies and (not implies[m] in formula):
            return False
    if not any((m in formula for m in required)):
        return False
    return True
