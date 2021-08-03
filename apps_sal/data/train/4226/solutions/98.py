def remove_smallest(numbers):
    if not numbers or len(numbers) == 1:
        return []
    smallest = min(numbers)
    numbers.remove(smallest)
    return numbers
