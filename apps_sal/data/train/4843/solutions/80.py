from itertools import combinations


def choose_best_sum(t, k, ls):
    l = [i for i in ls if i <= t]
    print(t, k, ls, l)
    try:
        return sorted([sum(i) for i in combinations(l, k) if sum(i) <= t])[-1]
    except:
        return None
