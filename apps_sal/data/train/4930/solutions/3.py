from itertools import combinations


def find_zero_sum_groups(a, n):
    li = sorted(map(sorted, filter(lambda x: sum(x) == 0, combinations(set(a), n))))
    return li if len(li) > 1 else li[0] if li else "No combinations" if a else "No elements to combine"
