import math


def vector_length(v):
    return math.sqrt(math.pow(v[0][0] - v[1][0], 2) + math.pow(v[0][1] - v[1][1], 2))
