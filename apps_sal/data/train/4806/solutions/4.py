class LCG(object):
    a, c, m = 2, 3, 10

    def __init__(self, seed):
        self.seed = seed
        self.x = seed

    def random(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x / self.m
