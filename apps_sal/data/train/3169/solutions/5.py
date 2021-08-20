from functools import lru_cache


@lru_cache()
def pentabonacci(n):
    return n if n in (0, 4) else 1 if n in (1, 2) else 2 if n == 3 else sum((pentabonacci(n - k) for k in range(1, 6)))


def count_odd_pentaFib(n):
    return sum((1 for i in range(n + 1) if pentabonacci(i) % 2)) - (1 if n > 1 else 0)
