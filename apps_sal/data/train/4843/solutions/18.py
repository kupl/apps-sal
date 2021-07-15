from itertools import combinations
def choose_best_sum(t, k, ls):
    closest = 0
    for x in combinations(ls, k):
        s = sum(x)
        if s == t:
            return t
        elif s < t:
            if t - closest > t - s:
                closest = s

    return closest if closest else None
