def remove_smallest(numbers):
    numbers = numbers[:]
    if not numbers:
        return numbers
    else:
        numbers.remove(min(numbers))
        return numbers
