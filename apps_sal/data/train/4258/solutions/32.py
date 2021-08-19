def series_sum(n):
    ls = []
    if n == 0:
        return str('%5.2f' % 0.0)[1:]
    for n in range(1, n):
        ls.append(1 / (1 + n * 3))
    return str('%5.2f' % float(sum(ls) + 1))[1:]
