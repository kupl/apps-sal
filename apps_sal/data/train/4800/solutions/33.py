def hotpo(n):
    res = 0
    while n != 1:
        res += 1
        n = n * 3 + 1 if n & 1 else n >> 1
    return res
