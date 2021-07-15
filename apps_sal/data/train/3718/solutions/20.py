def divisors(n):
    return sum(n % d == 0 for d in range(1, n + 1))
