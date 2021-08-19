from itertools import combinations


def counting_triangles(V):
    number = 0
    for i in sorted(combinations(V, 3)):
        (x, y, z) = sorted(i)
        if x + y > z:
            number += 1
    return number
