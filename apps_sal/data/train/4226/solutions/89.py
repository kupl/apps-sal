def remove_smallest(numbers):
    new_numbers = numbers.copy()
    try:
        new_numbers.remove(min(numbers))
    except ValueError:
        pass
    return new_numbers
