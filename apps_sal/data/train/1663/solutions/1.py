def count_divisors(n):
    return 2 * sum((n // i for i in range(1, int(n ** 0.5) + 1))) - int(n ** 0.5) ** 2
