def SumEvenFibonacci(n):
    a, b, r = 1, 1, 0
    while a <= n:
        a, b, r = b, a + b, r + (a & 1 < 1) * a
    return r
