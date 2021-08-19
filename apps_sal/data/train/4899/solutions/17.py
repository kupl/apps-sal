from math import exp


def weight(n, w):
    return w * (1 - exp(-2 * n)) * 0.17174117862516716
