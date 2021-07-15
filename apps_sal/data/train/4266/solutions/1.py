from numpy import dot

def min_dot(a, b):
    return dot(sorted(a), sorted(b, reverse=True))
