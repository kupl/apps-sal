from itertools import combinations


def find_zero_sum_groups(arr, n):
    if not arr:
        return "No elements to combine"
    res = {c for c in combinations(set(arr), n) if not sum(c)}
    if len(res) == 1:
        return sorted(res.pop())
    return sorted(map(sorted, res)) if res else "No combinations"
