def doubles(maxk, maxn):
    res = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            res += 1 / (k * (n + 1) ** (2 * k))
    return res
