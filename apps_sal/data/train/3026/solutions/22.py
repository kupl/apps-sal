from itertools import permutations


def min_value(digits):
    return sum(v * 10 ** i for i, v in enumerate(reversed(min(list(permutations(set(digits)))))))
