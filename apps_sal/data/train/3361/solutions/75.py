def sum_of_minimums(numbers):
    counter = 0
    for list in numbers:
        counter += min(list)
    return counter
