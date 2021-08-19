def choose_best_sum(t, k, ls):
    from itertools import combinations
    c = [i for i in combinations(ls, k)]
    l = []
    for i in c:
        l.append(sum(i))
    f = list(filter(lambda x: x <= t, l))
    return None if len(f) == 0 else max(f)
