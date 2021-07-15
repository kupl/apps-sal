def fusc(n):
    a, b = 1, 0
    while n > 0:
        if n & 1: b = a + b
        else: a = a + b
        n >>= 1
    return b      
