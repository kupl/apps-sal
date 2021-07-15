from functools import reduce

class Datamining:

    def __init__(self, train_set):
        self.p = train_set[:5]
    
    def lagrange_interp(self, x):
        return sum(reduce(lambda p,n: p*n, [(x-xi)/(xj-xi) for (i,(xi,yi)) in enumerate(self.p) if j!=i], yj) for (j,(xj,yj)) in enumerate(self.p))
    
    def predict(self, x):
        return self.lagrange_interp(x)
