def maxlen(L1, L2):
    a, b = sorted([L1, L2])
    if b < 2*a:
        return b / 2
    elif 2*a < b < 3*a:
        return a
    else:
        return b / 3
