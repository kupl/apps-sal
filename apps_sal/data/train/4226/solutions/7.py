def remove_smallest(numbers):
    copy = numbers.copy()
    if len(copy) > 0:
        copy.remove(min(copy))
    return copy
