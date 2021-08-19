def chsgn(k):
    r = []
    for x in k:
        if x < 0:
            r.append(-x)
        else:
            r.append(x)
    return r


def prod2sum(a, b, c, d):
    e1 = a * c + b * d
    f1 = a * d - b * c
    e2 = a * c - b * d
    f2 = a * d + b * c
    k = chsgn([e1, e2, f1, f2])
    e1 = k[0]
    e2 = k[1]
    f1 = k[2]
    f2 = k[3]
    if e1 == f2 and f1 == e2 or (e1 == e2 and f1 == f2):
        res = [[min(e1, f1), max(e1, f1)]]
    else:
        res = [[min(e1, f1), max(e1, f1)]]
        res.append([min(e2, f2), max(e2, f2)])
    res = sorted(res, key=lambda x: x[0])
    return res
