def remove_smallest(numbers):
    if numbers:
        new_numbers = numbers.copy()
        new_numbers.remove(min(numbers))
        return new_numbers
    else:
        return []
