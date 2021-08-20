def int_rac(n, x, c=1):
    return int_rac(n, (x + n / x) / 2, c + 1) if abs(int(n ** 0.5) - x) >= 1 else c
