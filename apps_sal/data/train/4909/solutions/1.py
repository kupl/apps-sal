import random as random_
del __import__('sys').modules['random']


class Random:

    def __init__(self, seed):
        self.rand = random_.Random(seed)

    def __setattr__(self, name, value):
        if name == 'seed':
            self.rand.seed(value)
        else:
            super(Random, self).__setattr__(name, value)

    def random(self):
        return self.rand.uniform(0, 1)

    def randint(self, start, end):
        return self.rand.randint(start, end)
