def max_sumDig_aux(nmax, maxsm):
    (res, i) = ([], 1000)
    while i <= nmax:
        a = list(str(i))
        (j, b) = (0, 0)
        while j <= len(a) - 4:
            if sum(map(int, a[j:j + 4])) <= maxsm:
                b += 1
            j += 1
        if b == j:
            res.append(i)
        i += 1
    return res


def max_sumDig(nmax, maxsm):
    res = max_sumDig_aux(nmax, maxsm)
    l = len(res)
    s = sum(res)
    m = s / float(l)
    d = list([(abs(x - m), x) for x in res])
    d.sort()
    return [l, d[0][1], s]
