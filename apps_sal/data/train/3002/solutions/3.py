def is_pronic(n):
    return n >= 0 and (1 + 4 * n) ** 0.5 % 1 == 0
