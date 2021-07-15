def isValid(a):
    for x, y in [[1,2], [3,4]]:
        if x in a and y in a: return False
    return (5 in a) == (6 in a) and any(x in a for x in (7,8))
