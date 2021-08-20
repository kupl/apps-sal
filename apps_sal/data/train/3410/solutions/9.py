def scratch(L):
    return sum((int(d) * (a == b == c) for x in L for (a, b, c, d) in [x.split()]))
