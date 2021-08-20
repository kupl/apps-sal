def distance(n):
    return (lambda s: 0 if n == 1 else s + abs(s - (n - 4 * s * s + 4 * s - 1) % (2 * s)))(int((n - 1) ** 0.5 + 1) >> 1)
