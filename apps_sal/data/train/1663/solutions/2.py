def count_divisors(n):
    return 2 * sum((n // k for k in range(int(n ** 0.5), 0, -1))) - int(n ** 0.5) ** 2
