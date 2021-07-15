def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return sum(numbers[:2])
