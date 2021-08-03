from functools import reduce


def elevator_distance(lst):
    return sum(abs(a - b) for a, b in zip(lst, lst[1:]))
