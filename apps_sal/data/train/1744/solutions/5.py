def fusc(n):
    a, b = 1, 0
    while n > 0: a, b, n = a + b * (1 - n & 1), a * (n & 1) + b, n >> 1
    return b    
