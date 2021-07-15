def sum_of_minimums(numbers):
    return sum(sorted(i, reverse=True).pop() for i in numbers)
