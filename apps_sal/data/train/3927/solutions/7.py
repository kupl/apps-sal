def dig_pow(n, p):
    (k, r) = divmod(sum((int(l) ** (p + i) for (i, l) in enumerate(str(n)))), n)
    return -1 if r else k
