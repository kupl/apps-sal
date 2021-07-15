def two_highest(arg1):
    l = list(set(arg1))
    l.sort()
    if len(l) >= 2:
        return [ l[-1], l[-2] ]
    elif len(l) == 1:
        return [ l[-1] ]
    else:
        return []

