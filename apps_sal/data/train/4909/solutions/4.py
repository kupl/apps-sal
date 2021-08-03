import math


class Random():
    def __init__(self, seed):
        self.seed = seed

    def random(self):
        x = math.sin(self.seed) * 10000
        self.seed = x
        return x - math.floor(x)

    def randint(self, start, end):
        return math.floor(self.random() * (end - start + 1)) + start
