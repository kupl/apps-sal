def solve(a, b):
    primes = [False, 2] + [x for x in range(3, b + 1, 2) if all((x % d for d in range(3, int(x ** 0.5 + 1), 2)))]
    dom_pos = [primes[x] for x in primes if x < len(primes)]
    return sum((x for x in dom_pos if a <= x <= b))
