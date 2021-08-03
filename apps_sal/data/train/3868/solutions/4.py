from itertools import combinations


def closest_sum(ints, num):
    return min(map(sum, combinations(ints, 3)), key=lambda x: abs(x - num))
