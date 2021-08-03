import math


def vector_length(vector):
    return math.hypot(vector[0][0] - vector[1][0],
                      vector[0][1] - vector[1][1])
