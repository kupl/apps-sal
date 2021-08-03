def sum_of_minimums(numbers):
    return sum(min(numbers[x]) for x in range(0, len(numbers)))
