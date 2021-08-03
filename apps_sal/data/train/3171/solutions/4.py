from functools import reduce


def crashing_weights(weights):
    return [reduce(lambda x, y: x * (x > y) + y, pile) for pile in zip(*weights)]
