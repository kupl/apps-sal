def alternate_sort(l):
    res = sorted(l, key=lambda x: abs(x))
    n = 1
    new_l = []
    while res:
        for x in res:
            if (x>=0, x<0)[n%2]:
                new_l.append(x)
                res.remove(x)
                break
        n += 1
    return new_l
