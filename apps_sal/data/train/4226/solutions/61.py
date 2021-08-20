def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        a = numbers.copy()
        b = a.remove(min(a))
        return a
