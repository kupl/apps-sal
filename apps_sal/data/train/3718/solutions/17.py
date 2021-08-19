def divisors(n):
    return 1 if n == 1 else 2 + sum((1 + (0 if k == n // k else 1) for k in range(2, int(n ** 0.5) + 1) if n % k == 0))
