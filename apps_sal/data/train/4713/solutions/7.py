from itertools import permutations


def late_clock(digits):
    decreasing_combos = permutations(sorted(digits, reverse=True))
    max_combo = next(c for c in decreasing_combos if c[:2] < (2, 4) and c[2] < 6)
    return "{}{}:{}{}".format(*max_combo)
