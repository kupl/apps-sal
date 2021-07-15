class Datamining:

    def __init__(self, train_set):
        total = len(train_set)
        x = []
        for i in train_set:
            x.append(i[0])
        y = []
        for i in train_set:
            y.append(i[1])
        xmean = sum(x)/total
        ymean = sum(y)/total
        a = 0
        b = 0
        for i in range(total):
            a += (x[i]-xmean) * (y[i] - ymean)
            b+= (x[i]-xmean)**2
        self.z = a/b
        self.y = ymean - (self.z*xmean)

    def predict(self, x):
        return x*self.z + self.y
        pass

