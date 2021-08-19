def sum_two_smallest_numbers(numbers):
    numbers.sort()
    subNumbers = numbers[:2]
    return sum(subNumbers)
