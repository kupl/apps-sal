def divisors(n):
    return sum((2 for d in range(1, int(n ** 0.5 + 1)) if not n % d)) - int((n ** 0.5).is_integer())
