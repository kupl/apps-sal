def sum_even_fibonacci(limit):
    if limit < 2:
        return 0
    a, b, total = 1, 2, 0
    while b <= limit:
        total += (b % 2 == 0) and b
        a, b = b, a + b
    return total


SumEvenFibonacci = sum_even_fibonacci
