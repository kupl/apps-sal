class Datamining:
    a = 0
    b = 0

    def __init__(self, train_set):
        sx = sy = sxx = sxy = 0
        n = len(train_set)
        for i in range(n):
            sx += train_set[i][0]
            sy += train_set[i][1]
            sxx += train_set[i][0] ** 2
            sxy += train_set[i][0] * train_set[i][1]
        self.b = (n * sxy - sx * sy) / (n * sxx - sx ** 2)
        self.a = (sy - self.b * sx) / n

    def predict(self, x):
        return self.a + self.b * x
