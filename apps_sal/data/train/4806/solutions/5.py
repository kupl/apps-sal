class LCG:
    a = 2
    c = 3
    m = 10

    def __init__(self, seed):
        self.x = seed

    def random(self):
        self.x = (self.a * self.x + self.c) % self.m
        return 1.0 * self.x / self.m
