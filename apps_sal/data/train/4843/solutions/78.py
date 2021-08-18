import itertools


def choose_best_sum(t, k, ls):
    print(t, k, ls)
    posible_roads = itertools.combinations(ls, k)
    under_posible = []
    for posibility in posible_roads:
        if sum(posibility) == t:
            return t
        elif sum(posibility) <= t:
            under_posible.append(sum(posibility))
    return sorted(under_posible)[-1] if under_posible else None
    print(sorted(under_posible))
