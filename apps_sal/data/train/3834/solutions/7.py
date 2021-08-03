def palin(a, b):
    l = str(10**((a + 1) // 2 - 1) + b - 1)
    return int(l + (l[::-1] if a % 2 == 0 else l[:-1][::-1]))
