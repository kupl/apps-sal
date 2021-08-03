from math import log2 as lg


def half_life(initial, remaining, time):
    return time / lg(initial / remaining)
