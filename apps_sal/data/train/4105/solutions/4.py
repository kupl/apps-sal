def sumDig_nthTerm(st, p, n):
    return sum(map(int, str(st + sum(p) * ((n - 1) // len(p)) + sum(p[:(n - 1) % len(p)]))))
