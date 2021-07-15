class LCG:
    def __init__(self, n):
        self.n = n
        
    def random(self):
        self.n = (self.n * 2 + 3) % 10
        return self.n / 10
