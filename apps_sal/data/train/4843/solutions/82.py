from itertools import combinations


def choose_best_sum(t, k, ls):
    sum_list = list(set(sum(i) for i in combinations(ls, k)))
    best = [9999999999, 0]
    for i in sum_list:
        if t - i >= 0 and t - i < best[0]:
            best[0], best[1] = t - i, i
    if best[1] == 0:
        return None
    else:
        return best[1]
