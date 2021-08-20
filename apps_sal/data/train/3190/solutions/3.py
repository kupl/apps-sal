from bisect import bisect_left, bisect


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))


def is_symmetry(n):
    return str(n ** 2)[:2] in SPRIMES


SPRIMES = [str(i) for i in range(11, 100, 2) if is_prime(i)]
BASE = [i for i in range(0, 100) if i * i % 100 == i]
candidates = (i + d for i in range(1100, 10000000 + 1, 100) if str(i)[:2] in SPRIMES for d in BASE)
NS = [x for x in candidates if is_symmetry(x)]


def solve(a, b):
    return bisect(NS, b - 1) - bisect_left(NS, a)
