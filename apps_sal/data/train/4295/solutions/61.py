from math import ceil


def balanced_num(number):
    (sum1, sum2) = (0, 0)
    number = list(str(number))
    for i in range(0, int(ceil(len(number) / 2) - 1)):
        sum1 += int(number[i])
        sum2 += int(number[-1 - i])
    if sum1 == sum2:
        return 'Balanced'
    return 'Not Balanced'
