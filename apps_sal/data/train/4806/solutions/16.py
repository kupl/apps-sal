class LCG(object):

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        (a, c, m) = (2, 3, 10)
        self.seed = (a * self.seed + c) % m
        return self.seed / 10.0
