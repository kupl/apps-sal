from itertools import combinations


def digits(num):
    return [int(a) + int(b) for a, b in combinations(str(num), 2)]
