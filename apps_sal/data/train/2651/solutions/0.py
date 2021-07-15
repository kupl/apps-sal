def prod2sum(a, b, c, d):
    e = sorted([abs(a*d-b*c), abs(a*c+b*d)])
    f = sorted([abs(a*c-b*d), abs(a*d+b*c)])
    if e == f:
        return [e]
    else:
        return sorted([e, f])


