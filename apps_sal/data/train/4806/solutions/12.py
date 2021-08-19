class LCG(object):
    (a, c, m) = (2, 3, 10)

    def __init__(self, seed):
        self.current = seed

    def random(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current / self.m
