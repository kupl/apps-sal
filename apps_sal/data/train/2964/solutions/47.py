def sum_two_smallest_numbers(numbers):
    ch1 = min(numbers)
    numbers.pop(numbers.index(ch1))
    ch2 = min(numbers)
    return ch1 + ch2
