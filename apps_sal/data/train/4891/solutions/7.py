class Datamining:

    def __init__(self, ts):
        self.N = len(ts)
        self.m = (self.N * sum((x * y for (x, y) in ts)) - sum((x for (x, _) in ts)) * sum((y for (_, y) in ts))) / (self.N * sum((x ** 2 for (x, _) in ts)) - sum((x for (x, _) in ts)) ** 2)
        self.b = (sum((y for (_, y) in ts)) - self.m * sum((x for (x, _) in ts))) / self.N

    def predict(self, x):
        return self.m * x + self.b
