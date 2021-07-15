def flatten(*a):
    r = []
    for x in a:
        if isinstance(x, list):
            r.extend(flatten(*x))
        else:
            r.append(x)
    return r
