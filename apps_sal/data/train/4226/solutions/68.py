def remove_smallest(numbers):
    numbers1 = numbers.copy()
    if len(numbers1) > 0:
        numbers1.remove(min(numbers1))
        return numbers1
    else:
        return numbers
