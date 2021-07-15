def remove_smallest(numbers):
    if numbers:
        a = sorted(numbers)
        b = numbers[:]
        b.remove(a[0])
        return b
    else:
        return []
