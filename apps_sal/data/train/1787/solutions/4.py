from functools import reduce


class Datamining:
    def __init__(self, train_set):
        self.s = train_set[:6]

    def predict(self, x):
        # Lagrange interpolating polynomial
        return sum(
            reduce(lambda s, n: s * n, [(x - xi) / (xj - xi) for (i, (xi, yi)) in enumerate(self.s) if j != i], yj) for
            (j, (xj, yj)) in enumerate(self.s))
