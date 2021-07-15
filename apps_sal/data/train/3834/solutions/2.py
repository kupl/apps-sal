def palin(a, b):
    half = str(10**((a + 1) // 2 - 1) + b - 1)
    return int(half + (half[::-1] if a % 2 == 0 else half[:-1][::-1]))
