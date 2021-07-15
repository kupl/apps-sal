def remove_smallest(numbers):
    r=numbers[:]
    if numbers:
        r.pop(numbers.index(min(numbers)))
    return r
