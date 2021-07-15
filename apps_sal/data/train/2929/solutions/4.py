def factors(n):
    sq = lambda x: x**2
    cb = lambda x: x**3
    return [[x for x in range(2, n) if n % sq(x) == 0], [x for x in range(2, n) if n % cb(x) == 0]]
