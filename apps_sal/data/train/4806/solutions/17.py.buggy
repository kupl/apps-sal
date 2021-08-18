class LCG(object):
    nonlocal a, c, m
    a = 2
    c = 3
    m = 10

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        self.seed = (a * self.seed + 3) % m
        return self.seed / 10
