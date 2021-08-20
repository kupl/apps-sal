from datetime import datetime


class Random:

    def __init__(self, seed):
        self.seed = seed
        self.x = self.next_x(self.seed)

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, seed):
        self.x = self.next_x(seed)
        self.__seed = seed

    def next_x(self, x):
        x = x ^ x << 13 & 4294967295
        x = x ^ x >> 17 & 4294967295
        x = x ^ x << 15 & 4294967295
        return x & 4294967295

    def random(self):
        x = self.x
        self.x = self.next_x(x)
        return x / 2 ** 32

    def randint(self, start, end):
        x = self.x
        self.x = self.next_x(x)
        return (end - start) * x // 2 ** 32 + start
