def remove_smallest(numbers):
    if not numbers:
        return []
    array = numbers[:]
    array.remove(min(numbers))
    return array
