def count_number(n, x):
    return (lambda r: len([i for i in range(1, int(r) + 1) if x % i == 0 and x / i <= n]) * 2 - (1 if r % 1 == 0 and r <= n else 0))(x ** 0.5)
