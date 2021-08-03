class Datamining:

    def __init__(self, train_set):
        self.X = [s[0] for s in train_set[:6]]
        self.Y = [s[1] for s in train_set[:6]]

    def predict(self, x):
        y = 0
        for j in range(len(self.X)):
            Lj, xj = 1, self.X[j]
            for k in range(len(self.X)):
                xk = self.X[k]
                if xk != xj:
                    Lj *= (x - xk) / (xj - xk)
            y += Lj * self.Y[j]

        return y
