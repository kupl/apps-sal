# A reason that it can be up to 10**10000 is so itertools.permutations will not work
from math import factorial


def sum_arrangements(num):
    return int(''.join(["1" for i in range(len(str(num)))])) * sum([int(i) for i in str(num)]) * factorial(len(str(num)) - 1)
