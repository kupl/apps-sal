from collections import defaultdict


def pair_of_shoes(shoes):
    sz = defaultdict(list)
    for i in shoes:
        sz[i[1]].append(i[0])
    return all((i[1].count(1) == i[1].count(0)) for i in sz.items())
