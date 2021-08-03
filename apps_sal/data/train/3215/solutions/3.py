def reduce_pyramid(base):
    tot, c, n = 0, 1, len(base) - 1
    for i in range(n + 1 >> 1):
        tot += c * (base[i] + base[n - i])
        c = c * (n - i) // (i + 1)
    if not n & 1:
        tot += c * base[n >> 1]
    return tot
