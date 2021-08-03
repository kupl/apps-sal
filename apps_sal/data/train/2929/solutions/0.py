def factors(n):
    sq = [a for a in range(2, n + 1) if not n % (a**2)]
    cb = [b for b in range(2, n + 1) if not n % (b**3)]
    return [sq, cb]
