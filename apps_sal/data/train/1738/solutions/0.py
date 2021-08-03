from collections import defaultdict
from itertools import combinations


def norme(vect): return sum(v**2 for v in vect)**.5
def vectorize(pt1, pt2): return [b - a for a, b in zip(pt1, pt2)]
def isInCircle(d, r): return d < r and (r - d) / r > 1e-10


def crossProd(v1, v2): return [v1[0] * v2[1] - v1[1] * v2[0],
                               v1[1] * v2[2] - v1[2] * v2[1],
                               v1[2] * v2[0] - v1[0] * v2[2]]


def biggest_triang_int(point_list, center, radius):
    filteredPts = [pt for pt in point_list if isInCircle(norme(vectorize(pt, center)), radius)]

    dctTriangles = defaultdict(list)
    for threePts in combinations(filteredPts, 3):
        area = abs(norme(crossProd(vectorize(*threePts[:2]), vectorize(*threePts[1:]))) / 2.0)
        if area > 1e-8:
            dctTriangles[area].append(list(threePts))

    maxArea = max(dctTriangles.keys()) if dctTriangles else 0
    return [] if not dctTriangles else [sum(map(len, dctTriangles.values())),
                                        maxArea,
                                        sorted(dctTriangles[maxArea]) if len(dctTriangles[maxArea]) > 1 else dctTriangles[maxArea][0]]
