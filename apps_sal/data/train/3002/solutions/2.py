def is_pronic(n):
    if n < 0:
        return False
    s = int(n ** 0.5)
    return s * (s + 1) == n
