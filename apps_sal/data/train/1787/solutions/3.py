from functools import reduce


class Datamining:
    def __init__(self, train_set):
        self.s = train_set[:6]

    def predict(self, x):
        def f(j, x, xj): return [(x - xi) / (xj - xi) for (i, (xi, yi)) in enumerate(self.s) if j != i]
        return sum(
            reduce(lambda s, n: s * n, f(j, x, xj), yj) for (j, (xj, yj)) in enumerate(self.s))
