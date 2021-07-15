def sum_pow_dig_seq(start, n, k):
    li = []
    for _ in range(k):
        r = sum([j ** n for j in map(int, str(start))])
        if r in li:
            reach = n = li.index(r) + 1 ; series = li[li.index(r):] ; s_l = len(series)
            while n + s_l <= k : n += s_l
            return [reach, series, s_l, series[k - n]]
        li.append(r) ; start = r
