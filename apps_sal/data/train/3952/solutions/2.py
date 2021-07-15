from math import log


def half_life(initial, remaining, time):
    return time*log(2.0)/log(initial/remaining)
