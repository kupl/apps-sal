class Datamining:

    def __init__(self, train_set):
        (a_x, a_y) = ([], [])
        for (x, y) in train_set:
            a_x.append(x)
            a_y.append(y)
        mean_x = sum(a_x) / len(a_x)
        mean_y = sum(a_y) / len(a_y)
        cov = sum(((x - mean_x) * (y - mean_y) for (x, y) in train_set))
        x_v = sum(((x - mean_x) ** 2 for x in a_x))
        self.a = cov / x_v
        self.b = mean_y - self.a * mean_x

    def predict(self, x):
        return self.a * x + self.b
