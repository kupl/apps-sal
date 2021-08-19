from functools import reduce


def prod(u):
    p = 1
    for x in u:
        p *= x
    return p


cache = {}


def part_aux(s, k):
    k0 = min(s, k)
    if k0 < 1:
        return []
    i = (s - 1) * s / 2 + k0 - 1
    ret = cache.get(i)
    if ret:
        return ret
    res = []
    for n in range(k0, 0, -1):
        r = s - n
        if r > 0:
            for t in part_aux(r, n):
                if type(t) is list:
                    res.append([n] + t)
                else:
                    res.append([n, t])
        else:
            res.append([n])
    cache[i] = res
    return res


def part(n):
    from functools import reduce
    r = sorted(set(map(prod, part_aux(n, n))))
    lg = len(r)
    avg = reduce(lambda x, y: x + y, r, 0) / float(lg)
    rge = r[lg - 1] - r[0]
    md = (r[(lg - 1) // 2] + r[lg // 2]) / 2.0
    return 'Range: %d Average: %.2f Median: %.2f' % (rge, avg, md)
