def hotpo(n):
    if n == 1:
        return 0
    else:
        return 1 + (hotpo(n * 3 + 1) if n % 2 else hotpo(int(n / 2)))
