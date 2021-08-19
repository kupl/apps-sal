class Random:

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        self.seed = (4123 * self.seed + 4321) % 4096
        return self.seed / 4096

    def randint(self, start, end):
        return int(start + (end - start) * self.random())
