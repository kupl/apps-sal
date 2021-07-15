def remove_smallest(numbers):
    if numbers:
        x = numbers[:]
        x.remove(min(x))
        return x
    else:
        return []
