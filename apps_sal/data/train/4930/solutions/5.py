from itertools import combinations


def find_zero_sum_groups(arr, n):
    if not arr:
        return 'No elements to combine'
    res = [list(c) for c in combinations(sorted(set(arr)), n) if not sum(c)]
    if not res:
        return 'No combinations'
    if not res[1:]:
        return res[0]
    return res
