class Datamining:
    
    def __init__(self, train_set):
        x_mean = lambda train_set: sum( [i[0] for i in train_set] ) / len( [i[0] for i in train_set] )
        y_mean = lambda train_set: sum( [i[1] for i in train_set] ) / len( [i[1] for i in train_set] )
        f = lambda x_mean, y_mean, train_set: sum( (x - x_mean) * (y - y_mean) for x, y in train_set )
        g = lambda x_mean, train_set: sum( (x - x_mean) ** 2 for x in [i[0] for i in train_set] )
        self.a = f( x_mean(train_set), y_mean (train_set), train_set ) / g ( x_mean (train_set), train_set )
        self.b = y_mean(train_set) - self.a * x_mean(train_set)
        
    def predict(self, x): return x * self.a + self.b
