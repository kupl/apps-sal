import itertools
import math


def sum_arrangements(num):
    return math.factorial(len(str(num)) - 1) * (int("1" * len(str(num)))) * sum(int(i) for i in str(num))
