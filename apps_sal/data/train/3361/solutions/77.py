def sum_of_minimums(numbers):
    total = 0
    for value in range(len(numbers)):
        total += min(numbers[value])
    return total

