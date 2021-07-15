def sum_two_smallest_numbers(numbers):
    first, second = float('inf'), float('inf')
    for n in numbers:
        if n < first:
            first, second = n, first
        elif n < second:
            second = n
    return first + second
