import math


def evaporator(content, e, t):
    return math.ceil(math.log(t / 100) / math.log(1 - e / 100))
