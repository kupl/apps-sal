def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))
