import itertools


def choose_best_sum(t, k, ls):
    comb = itertools.combinations(ls, k)
    list1 = [sum(combin) for combin in comb if sum(combin) <= t]
    return None if list1 == [] else max(list1)
