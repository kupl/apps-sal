def fusc(n):
    assert type(n) == int and n >= 0
    if n < 2:
        return n
    if n & 1:
        return fusc((n - 1) // 2) + fusc((n - 1) // 2 + 1)
    return fusc(n // 2)
