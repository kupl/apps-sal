def combos(n, m = 1):
    if n < m:return []
    res = [[n]]
    for i in xrange(m, n):
        l = [i]
        for j in combos(n - i, i):
           res += [l + j]
    return res
