import itertools


def choose_best_sum(t, k, ls):
    distances = []
    for comb in itertools.combinations(ls, k):
        if sum(comb) <= t:
            distances.append(sum(comb))
    return None if not distances else max(distances)
