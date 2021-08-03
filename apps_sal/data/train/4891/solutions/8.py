class Datamining:

    def __init__(self, train_set):
        n = len(train_set)
        xbar = sum([s[0] for s in train_set]) / n
        ybar = sum([s[1] for s in train_set]) / n
        print(xbar, ybar)
        xe = [s[0] - xbar for s in train_set]
        ye = [s[1] - ybar for s in train_set]
        self.beta = sum(xe[i] * ye[i] for i in range(n)) / sum(xe[i] ** 2 for i in range(n))
        self.alpha = ybar - self.beta * xbar
        predict = [self.alpha + self.beta * s[0] for s in train_set]

    def predict(self, x):
        return self.alpha + self.beta * x
