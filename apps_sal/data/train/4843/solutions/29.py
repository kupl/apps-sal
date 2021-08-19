from itertools import combinations


def choose_best_sum(t, k, ls):
    maxx = 0
    list(combinations(ls, k))
    for i in list(combinations(ls, k)):
        if sum(i) > t:
            pass
        elif sum(i) > maxx:
            maxx = sum(i)
    if maxx == 0:
        return None
    else:
        return maxx
