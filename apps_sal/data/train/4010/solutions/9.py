from itertools import combinations as C


def counting_triangles(V):
    return sum(a + b > c for a, b, c in C(sorted(V), 3))
