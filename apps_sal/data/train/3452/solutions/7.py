def snail(c, d, n):
    return max([i for i in range(c) if i * d - (n * i - n) >= c][0], 1)
