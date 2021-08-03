def remove_smallest(numbers):
    if numbers:
        numbers = numbers.copy()
        numbers.remove(min(numbers))
    return numbers
