from itertools import combinations


def closest_sum(ints, num):
    ss = map(sum, combinations(ints, 3))
    return min(ss, key=lambda x: abs(x - num))
