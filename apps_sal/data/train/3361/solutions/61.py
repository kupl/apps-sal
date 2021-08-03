def sum_of_minimums(numbers):
    min = 0

    for n in numbers:
        n.sort()
        min += n[0]
    return min
