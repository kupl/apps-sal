def SumEvenFibonacci(limit):
    a, b, result = 1, 2, 0
    while b <= limit:
        if b % 2 == 0:
            result += b
        a, b = b, a + b
    return result
