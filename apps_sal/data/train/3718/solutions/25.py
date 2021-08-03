def divisors(n):
    pass
    return [n % i for i in range(1, (n // 2) + 1)].count(0) + 1
