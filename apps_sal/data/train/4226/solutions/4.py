def remove_smallest(numbers):
    if not numbers:
        return numbers
    else:
        new = numbers[:]
        new.remove(min(numbers))
    return new
