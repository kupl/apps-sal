def divisors(n):
    return 1 + sum((1 for x in range(1, n // 2 + 1) if n % x == 0))
