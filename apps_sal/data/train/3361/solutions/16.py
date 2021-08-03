def sum_of_minimums(numbers):
    summ = 0
    for i in numbers:
        x = sorted(i)[0]
        summ += x

    return summ
