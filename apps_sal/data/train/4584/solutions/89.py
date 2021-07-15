def invert(lst):
    l = []
    if not lst:
        return l
    elif lst:
        for i in lst:
            l.append(~i + 1)
        return l

