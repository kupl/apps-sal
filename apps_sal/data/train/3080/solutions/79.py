def who_is_paying(n):
    nn = n[:2] if len(n) > 2 else n
    return [n] if n == nn else [n, nn]
