def remove_smallest(numbers):
    return numbers[0:numbers.index(min(numbers))] + numbers[numbers.index(min(numbers)) + 1:] if numbers else numbers
