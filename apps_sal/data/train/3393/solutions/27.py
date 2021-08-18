from math import sqrt


def list_squared(m, n):
    def F(x): return sum(b**2 + ((x / b)**2 if b * b != x else 0) for b in [a for a in range(1, int(sqrt(x)) + 1) if x % a == 0])
    return [[d, F(d)] for d in range(m, n + 1) if sqrt(F(d)).is_integer()]
