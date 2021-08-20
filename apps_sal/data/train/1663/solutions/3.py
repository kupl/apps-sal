def count_divisors(n):
    x = int(n ** 0.5)
    return 2 * sum((n // y for y in range(1, x + 1))) - x ** 2
