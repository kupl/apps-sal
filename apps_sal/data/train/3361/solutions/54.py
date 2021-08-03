def sum_of_minimums(numbers):
    sum = 0

    for i in range(0, len(numbers)):
        sum = sum + min(numbers[i])
        i = i + 1

    return sum
