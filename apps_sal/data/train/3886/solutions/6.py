def is_prime(n):
    return n > 1 and all((n % d for d in range(2, int(n ** 0.5) + 1)))


def total(arr):
    return sum((e for (i, e) in enumerate(arr) if is_prime(i)))
