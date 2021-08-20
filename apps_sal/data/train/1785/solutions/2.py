from math import *


def dithering(x, y):

    def di2(x):
        if x == 1:
            for i in [(0, 0), (1, 1), (1, 0), (0, 1)]:
                yield i
        else:
            for (i, j) in di2(x - 1):
                for (a, b) in di2(1):
                    yield (i + a * 2 ** (x - 1), j + b * 2 ** (x - 1))
    for i in di2(int(ceil(log(max(x, y), 2)))):
        if i[0] < x and i[1] < y:
            yield i
