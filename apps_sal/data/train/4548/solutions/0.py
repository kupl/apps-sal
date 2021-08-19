def SumEvenFibonacci(limit):
    (a, b, s) = (1, 1, 0)
    while a <= limit:
        if not a % 2:
            s += a
        (a, b) = (b, a + b)
    return s
