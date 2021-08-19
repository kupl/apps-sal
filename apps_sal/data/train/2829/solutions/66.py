def array_madness(a, b):
    sum1 = 0
    sum2 = 0
    for val1 in a:
        sum1 += val1 ** 2
    for val2 in b:
        sum2 += val2 ** 3
    return sum1 > sum2
