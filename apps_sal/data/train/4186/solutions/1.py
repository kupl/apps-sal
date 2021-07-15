def sum_of_threes(n):
    k, p = 0, []
    while n >= 3 ** k:
        k += 1
    while k >= 0:
        k -= 1
        if n >= 3 ** k:
            p.append("3^%d" % k)
            n -= 3 ** k
    return "Impossible" if n else '+'.join(p)
