def get_primes(n, m):
    return (tuple(g) for g in zip(*[iter([2] + [p for p in range(3, 15 * n, 2) if all((p % d for d in range(3, int(p ** 0.5) + 1, 2)))][:n - 1] + [None] * (m - 1))] * m))
