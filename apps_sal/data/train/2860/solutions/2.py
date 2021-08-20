def isomorph(s, t):
    if len(s) != len(t):
        return False
    p = set(zip(s, t))
    return all((len(p) == len(set(c)) for c in zip(*p)))
