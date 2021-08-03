from math import log2


def sequence(i):
    if i == 0:
        return 0
    e = int(log2(i))
    return 3**e + sequence(i - 2**e)
