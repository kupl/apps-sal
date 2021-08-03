class LCG(object):
    def __init__(self, x):
        self._seed = x

    def random(self):
        self._seed = (2 * self._seed + 3) % 10
        return self._seed / 10
