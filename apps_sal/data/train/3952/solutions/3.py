from math import log2

def half_life(initial, remaining, time):
    return time / log2(initial / remaining)
