from math import *


def half_life(initial, remaining, time):
    return time * log(.5) / log(remaining / initial)
