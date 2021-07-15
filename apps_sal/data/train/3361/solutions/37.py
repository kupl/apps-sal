def sum_of_minimums(numbers):
    sum = 0
    for n in range(len(numbers)):
        sum += sorted(numbers[n])[0]
    return sum
