def performant_smallest(xs, n):
    ys = sorted(xs)
    del ys[n:]
    m = ys[-1]
    km = ys.count(m)
    res = []
    for x in xs:
        if x <= m:
            if x < m:
                res.append(x)
            elif km > 0:
                res.append(x)
                km -= 1
    return res
