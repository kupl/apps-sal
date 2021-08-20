from collections import defaultdict


def pair_of_shoes(shoes):
    D = defaultdict(lambda: defaultdict(int))
    for (type, size) in shoes:
        D[size][type] += 1
    return all((v[0] == v[1] for v in D.values()))
