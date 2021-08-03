def remove_smallest(numbers):
    if numbers == []:
        return []
    numbers = numbers.copy()
    numbers.remove(min(numbers))
    return numbers
