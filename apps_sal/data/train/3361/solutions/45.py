def sum_of_minimums(numbers):
    b = []
    for i in range(0, len(numbers)):
        b.append(min(numbers[i]))
    c = 0
    for j in range(0, len(b)):
        c += b[j]
    return c
