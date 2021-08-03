from functools import reduce


def crashing_weights(weights):
    return reduce(lambda a, b: [a1 + b1 if a1 > b1 else b1 for a1, b1 in zip(a, b)], weights)
