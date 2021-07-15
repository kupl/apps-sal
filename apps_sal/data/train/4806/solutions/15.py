class LCG(object):

    def __init__(self, seed):
        self.seed = seed
        self.a = 2
        self.c = 3
        self.m = 10

    def random(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / 10
