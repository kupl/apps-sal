class Random:

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        self.seed = (432544 * self.seed + 1) % 1000000
        return self.seed / 1000000

    def randint(self, start, end):
        self.seed = (13 * self.seed + 1) % (end - start + 1)
        return self.seed + start
