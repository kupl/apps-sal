def dig_pow(n, p):
    s = sum((int(d) ** (p + i) for (i, d) in enumerate(str(n))))
    return s / n if s % n == 0 else -1
