def paperwork(n=5, m=5):
    if n + 0 < 0:
        return 0
    if m + 0 < 0:
        return 0
    x = n * m
    if x < 0:
        return 0
    return x
