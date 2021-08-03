def over_the_road(address, n):
    l = range(1, n * 2, 2)
    r = range(n * 2, 0, -2)
    if address % 2:
        return r[l.index(address)]
    else:
        return l[r.index(address)]
