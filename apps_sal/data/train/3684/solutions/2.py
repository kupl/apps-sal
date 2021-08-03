from numpy import dot


def is_orthogonal(u, v):
    return not dot(u, v)
