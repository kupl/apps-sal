def isValid(formula):
    a, b = sum([1 for c in formula if c in [1, 2]]), sum([1 for c in formula if c in [3, 4]])
    c, d = sum([1 for c in formula if c in [5, 6]]), sum([1 for c in formula if c in [7, 8]])

    return True if (a in range(2) and b in range(2)) and ((c == 0 or c == 2) and (d in range(1, 3))) else False
