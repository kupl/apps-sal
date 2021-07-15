
class Random():
    def __init__(self, seed):
        self.seed = seed
        self.r_it = self.r()
        
    def random(self):
        return next(self.r_it) / 2**32
    
    def randint(self, start, end):
        return int(start + (1 + end - start) * next(self.r_it) / 2**32)
    
    def r(self, m=2**32, a=1103515245, c=12345):
        while True:
            self.seed = (a * self.seed + c) % m
            yield self.seed

