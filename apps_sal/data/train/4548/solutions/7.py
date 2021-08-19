def fibonacci(max):
    (a, b) = (1, 2)
    while a <= max:
        yield a
        (a, b) = (b, a + b)


def SumEvenFibonacci(limit):
    return sum((n for n in fibonacci(limit) if n % 2 == 0))
