class Datamining:

    def __init__(self, train_set):
        n = len(train_set)
        M1 = [i[0] for i in train_set]
        M2 = [i[1] for i in train_set]
        x_mean = sum(M1) / n
        y_mean = sum(M2) / n
        numerator = 0
        denominator = 0
        for i in range(n):
            numerator += (M1[i] - x_mean) * (M2[i] - y_mean)
            denominator += (M1[i] - x_mean) ** 2
        self.n = numerator / denominator
        self.o = y_mean - (self.n * x_mean)
  
    def predict(self, x):
        return x*self.n + self.o
