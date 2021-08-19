def factor_sum(n):
    while True:
        (t, s, d) = (n, 0, 2)
        while d * d <= t:
            while t % d == 0:
                s += d
                t //= d
            d += 1
        if t > 1:
            s += t
        if s == n:
            return s
        n = s
