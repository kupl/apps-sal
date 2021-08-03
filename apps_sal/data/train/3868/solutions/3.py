from itertools import combinations


def closest_sum(ints, num):
    return sum(min(combinations(ints, 3), key=lambda i: abs(num - sum(i))))
