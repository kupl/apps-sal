import math


def power_of_two(x):
    return not bin(x)[2:].count('1') - 1 if x != 0 else False
