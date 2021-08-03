from math import sqrt


def vector_length(v):
    return sqrt((v[1][0] - v[0][0])**2 + (v[0][1] - v[1][1])**2)
