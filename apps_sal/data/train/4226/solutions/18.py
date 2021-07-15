def remove_smallest(numbers):
    if numbers:
        a = list(numbers)
        a.remove(min(a))
        return a
    return numbers
