def sum_of_minimums(numbers):
    t=0
    for i in range(len(numbers)):
        x = min(numbers[i])
        t += x
    return t
