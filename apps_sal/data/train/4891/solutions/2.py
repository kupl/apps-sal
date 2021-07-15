from operator import itemgetter

class Datamining:
    def __init__(self, train_set):
        X, Y = map(lambda L: sum(L)/len(train_set), zip(*train_set))
        COV = sum((x-X)*(y-Y) for x,y in train_set)
        VAR = sum((x-X)**2 for x in map(itemgetter(0), train_set))
        self.A = COV / VAR
        self.B = Y - self.A * X

    def predict(self, x):
        return self.A * x + self.B
