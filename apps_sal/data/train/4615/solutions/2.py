from sklearn.neighbors import NearestNeighbors
from itertools import product


def logistic_map(width, height, xs, ys):
    if not xs:
        return [[None] * width for _ in range(height)]
    neigh = NearestNeighbors(1, metric='manhattan')
    neigh.fit(list(zip(ys, xs)))
    it = iter(neigh.kneighbors(list(product(range(height), range(width))))[0])
    return [[next(it)[0] for _ in range(width)] for _ in range(height)]
