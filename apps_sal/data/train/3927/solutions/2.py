def dig_pow(n, p):
    t = sum((int(d) ** (p + i) for (i, d) in enumerate(str(n))))
    return t // n if t % n == 0 else -1
