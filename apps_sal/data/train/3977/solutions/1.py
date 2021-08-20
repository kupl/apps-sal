import math
import random


def cluster(points, n):

    def distance(c1, c2):
        s = 0
        for p1 in c1:
            for p2 in c2:
                s += math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return float(s) / (len(c1) * len(c2))

    def closest(cs):
        (min_dist, i1, i2) = (float('inf'), -1, -1)
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                dist = distance(cs[i], cs[j])
                if dist < min_dist:
                    min_dist = dist
                    (i1, i2) = (i, j)
        return (i1, i2)

    def merge(cs, i1, i2):
        cs[i1].extend(cs[i2])
        del cs[i2]
    clusts = [[x] for x in points]
    while len(clusts) > n:
        (ind1, ind2) = closest(clusts)
        merge(clusts, ind1, ind2)
    for i in range(len(clusts)):
        clusts[i] = sorted(clusts[i])
    return list(sorted(clusts))
