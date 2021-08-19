# Linear Congruential Generator (a pseudo random number generator)
class LCG(object):
    a = 2
    c = 3
    m = 10

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        next_random_num = self.a * self.seed + self.c
        next_random_num = next_random_num % self.m
        self.seed = next_random_num
        return next_random_num / 10
