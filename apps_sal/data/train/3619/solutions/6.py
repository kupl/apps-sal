def is_dd(n):
    n = str(n)
    return any(n.count(d) == int(d) for d in set(n))
