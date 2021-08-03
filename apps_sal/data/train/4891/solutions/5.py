class Datamining:
    def __init__(self, train_set):
        x_mean = sum([i[0] for i in train_set]) / len([i[0] for i in train_set])
        y_mean = sum([i[1] for i in train_set]) / len([i[1] for i in train_set])
        self.a = (sum((x - x_mean) * (y - y_mean) for x, y in train_set)) / \
                 (sum((x - x_mean) ** 2 for x in [i[0] for i in train_set]))
        self.b = y_mean - self.a * x_mean

    def predict(self, x): return x * self.a + self.b
