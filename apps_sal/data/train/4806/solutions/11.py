class LCG(object):

    def __init__(self, seed):
        self.seed = seed
        self.multiplier = 2
        self.increment = 3
        self.modulus = 10

    def random(self):
        self.seed = (self.multiplier * self.seed + self.increment) % self.modulus
        return self.seed / self.modulus
