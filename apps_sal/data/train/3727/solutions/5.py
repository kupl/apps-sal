def pythagorean_triplet(n):
    for k in range(1, int(n ** (1 / 3))):
        if n % k ** 3:
            continue
        for p in range(1, int((n // k ** 3) ** .2) + 1):
            for q in range(1, p):
                a, b, c = p * p - q * q, 2 * p * q, p * p + q * q
                if k**3 * a * b * c == n:
                    return sorted([k * a, k * b, k * c])
