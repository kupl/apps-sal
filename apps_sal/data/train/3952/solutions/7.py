import math


def half_life(initial, remaining, time):
    return time / math.log2(initial / remaining)
