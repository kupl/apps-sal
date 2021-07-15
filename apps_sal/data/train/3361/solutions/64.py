def sum_of_minimums(numbers):
    minimum = 0
    for i in range(len(numbers)):
        minimum +=min(numbers[i])
    return minimum
