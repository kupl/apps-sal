def SumEvenFibonacci(limit):
    a, b, result = 1, 2, 0
    while (a <= limit):
        if(not a & 1):
            result += a
        a, b = b, a + b
    return result
