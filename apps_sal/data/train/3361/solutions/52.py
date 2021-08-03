def sum_of_minimums(numbers):
    summ = 0

    for i in range(len(numbers)):
        mini = min(numbers[i])
        summ += mini
    return summ
