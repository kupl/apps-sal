def remove_smallest(numbers):
    if len(numbers) <= 1:
        return []
    numbers.remove(min(numbers))
    return numbers
