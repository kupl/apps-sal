def calc(a):
    sum = 0
    for i in range(len(a)):
        value = a[i]
        if value > 0:
            value *= value
        if (i + 1) % 3 == 0:
            value *= 3
        if (i + 1) % 5 == 0:
            value = -value
        sum += value
    return sum
