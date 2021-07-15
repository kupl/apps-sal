def isValid(a):
    b = not ((1 in a) and (2 in a))
    c = not ((3 in a) and (4 in a))
    d = ((5 in a) == (6 in a))
    e = ((7 in a) or (8 in a))
    print([b,c,d,e])
    return all([b,c,d,e])

