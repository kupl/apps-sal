def sum_two_smallest_numbers(numbers):
    min_1 = min(numbers)
    numbers.remove(min_1)
    min_2 = min(numbers)
    return min_1 + min_2
