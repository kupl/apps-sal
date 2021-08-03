from itertools import combinations


def choose_best_sum(t, k, ls):
    s = ([sum(b) for b in (list(combinations(ls, k))) if sum(b) <= t])
    if s == []:
        return None
    else:
        return max(s)
