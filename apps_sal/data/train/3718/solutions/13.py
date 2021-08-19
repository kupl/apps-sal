def divisors(n):
    return sum((1 for e in range(1, n + 1) if n % e == 0))
