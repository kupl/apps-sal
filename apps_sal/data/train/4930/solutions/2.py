from itertools import combinations


def find_zero_sum_groups(lst, n):
    if not lst:
        return "No elements to combine"
    result = [list(c) for c in combinations(sorted(set(lst)), n) if sum(c) == 0]
    return (result[0] if len(result) == 1 else result) or "No combinations"
