import numpy as np
from itertools import product


def fit_bag(h, w, items):
    items = sorted(map(np.array, items), key=lambda i: np.prod(i.shape), reverse=True)
    bag = np.zeros((h, w), dtype=int)

    def fit_bag_rec(bag, items, n=0):
        item = items[n]
        (itemH, itemW) = item.shape
        for (i, j) in product(range(h - itemH + 1), range(w - itemW + 1)):
            if not (bag[i:i + itemH, j:j + itemW] * item).any():
                bag[i:i + itemH, j:j + itemW] += item
                if n == len(items) - 1:
                    yield bag
                else:
                    yield from fit_bag_rec(bag, items, n + 1)
                bag[i:i + itemH, j:j + itemW] -= item
    return next(fit_bag_rec(bag, items)).tolist()
