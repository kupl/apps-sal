class Datamining:

    def __init__(self, train_set):
        n = len(train_set)
        X = [i[0] for i in train_set]
        Y = [i[1] for i in train_set]
        x_mean = sum(X) / n
        y_mean = sum(Y) / n
        numerator = 0
        denominator = 0
        for i in range(n):
            numerator += (X[i] - x_mean) * (Y[i] - y_mean)
            denominator += (X[i] - x_mean) ** 2
        self.b1 = numerator / denominator
        self.b0 = y_mean - self.b1 * x_mean

    def predict(self, x):
        return x * self.b1 + self.b0
