from itertools import combinations, permutations


def choose_best_sum(t, k, ls):
    print(t, k, ls)
    if k > int(len(ls)):
        return None
    new = []
    for i in list(combinations(ls, k)):
        new.append(sum(i))
    for i in sorted(new, reverse=True):
        if i <= t:
            return i
    return None
