from itertools import combinations


def counting_triangles(V):
    return sum(sum(comb) > 2 * max(comb) for comb in combinations(V, 3))
