import math


def reindeer(presents):

    p = math.ceil(presents / 30)

    if p > 6:

        raise ValueError("Error")

    else:

        return p + 2
