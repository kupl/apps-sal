import numpy as np
from itertools import combinations, product, starmap
from sklearn.cluster import KMeans

# Doesn't work for big tests, too bad


def cluster_kmeans(points, n):
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(points)
    res = [[] for _ in range(n)]
    for i, p in zip(kmeans.labels_, points):
        res[i].append(p)
    return sorted(map(sorted, res))


memo_points = {}


def point_dist(p1, p2):
    key = (p1, p2) if p1 < p2 else (p2, p1)
    if not key in memo_points:
        memo_points[key] = np.linalg.norm(np.array(key[0]) - np.array(key[1]))
    return memo_points[key]


memo_clusters = {}


def cluster_dist(clusters):
    key = tuple(map(tuple, clusters))
    if not key in memo_clusters:
        memo_clusters[key] = np.mean(list(starmap(point_dist, product(*key))))
    return memo_clusters[key]


def cluster(points, n):
    clusters = [[p] for p in points]
    while len(clusters) > n:
        c1, c2 = min(combinations(clusters, 2), key=cluster_dist)
        c1.extend(c2)
        clusters.remove(c2)
    return sorted(map(sorted, clusters))
