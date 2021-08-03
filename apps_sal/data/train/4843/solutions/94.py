from itertools import combinations


def choose_best_sum(t, k, ls):
    tp = []
    for m in combinations(ls, k):
        if sum(m) <= t:
            if sum(m) == t:
                return sum(m)
            tp.append(sum(m))
    return max(tp) if len(tp) > 0 else None
