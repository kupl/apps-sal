def SumEvenFibonacci(n):
    (s, a, b) = (0, 1, 2)
    while b <= n:
        (a, b, s) = (b, a + b, s + (1 - b % 2) * b)
    return s
