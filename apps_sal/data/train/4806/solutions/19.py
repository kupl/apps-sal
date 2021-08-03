class LCG(object):
    a = 2
    c = 3
    m = 10

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        self.seed = (LCG.a * self.seed + LCG.c) % LCG.m
        return self.seed / LCG.m
