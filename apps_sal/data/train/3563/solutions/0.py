def distance(n):
    if n == 1:
        return 0
    r = 0 - (1 - n ** 0.5) // 2
    (d, m) = divmod(n - (2 * r - 1) ** 2 - 1, 2 * r)
    z = (r * (1 + 1j) - m - 1) * 1j ** d
    return abs(z.real) + abs(z.imag)
