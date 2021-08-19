from math import factorial


def sum_arrangements(num):
    return int(''.join(['1' for i in range(len(str(num)))])) * sum([int(i) for i in str(num)]) * factorial(len(str(num)) - 1)
