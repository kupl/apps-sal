def sum_two_smallest_numbers(numbers):
    n1 = min(numbers)
    n2 = max(numbers)
    for n in numbers:
        if n1 < n < n2:
            n2 = n
    return n1 + n2
