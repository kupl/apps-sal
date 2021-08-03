def factors(n):
    def sq(x): return x**2
    def cb(x): return x**3
    return [[x for x in range(2, n) if n % sq(x) == 0], [x for x in range(2, n) if n % cb(x) == 0]]
