from itertools import combinations


def shortest_time(xs, ys=[]):
    if len(xs) == 2:
        return max(xs)
    result = 999999999
    for i, j in combinations(range(len(xs)), 2):
        m = max(xs[i], xs[j])
        xs2 = xs[:i] + xs[i + 1:j] + xs[j + 1:]
        ys2 = ys + [xs[i], xs[j]]
        for k, y in enumerate(ys2):
            result = min(m + y + shortest_time(xs2 + [y], ys2[:k] + ys2[k + 1:]), result)
    return result
