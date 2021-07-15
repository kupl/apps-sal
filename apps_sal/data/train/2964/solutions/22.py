def sum_two_smallest_numbers(numbers):
    a = min(numbers)
    b = min(numbers, key=lambda n: (n==a, n))
    return a+b
