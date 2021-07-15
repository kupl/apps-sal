def nth_floyd(n):
    a = (n * 8 + 1) ** 0.5
    return a // 2 if a % 1 <= 1e-10 else round(a / 2)
