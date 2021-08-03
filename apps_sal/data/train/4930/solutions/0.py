from itertools import combinations


def find_zero_sum_groups(arr, n):
    combos = sorted(sorted(c) for c in combinations(set(arr), n) if sum(c) == 0)
    return combos if len(combos) > 1 else combos[0] if combos else "No combinations" if arr else "No elements to combine"
