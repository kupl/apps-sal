class Random:

    def __init__(self, seed):
        self.seed = (seed if seed else 305419896) & 4294967295

    def randint(self, start, end):
        return int(self.random() * (end - start + 1) + start)

    def random(self):
        x = self.seed
        x ^= x << 13 & 4294967295
        x ^= x >> 17
        x ^= x << 5 & 4294967295
        self.seed = x
        return x / (1 << 32)
