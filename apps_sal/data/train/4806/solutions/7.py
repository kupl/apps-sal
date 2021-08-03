class LCG(object):
    a = 2
    c = 3
    m = 10

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        result = (self.a * self.seed + self.c) % self.m
        self.seed = result
        return result / 10.0
