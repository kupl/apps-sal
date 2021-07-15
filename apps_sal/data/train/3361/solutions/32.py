def sum_of_minimums(numbers):
    return sum(sorted(i).pop(0) for i in numbers)
