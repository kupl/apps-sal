def find_difference(a, b):
    sum1 = 1
    sum2 = 1
    for i in a:
        sum1 = sum1 * i
    for j in b:
        sum2 = sum2 * j
    return abs(sum1 - sum2)
