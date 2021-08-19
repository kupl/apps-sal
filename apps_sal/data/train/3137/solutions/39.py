import math


def round_it(n):
    mat = str(n).split('.')
    if len(mat[0]) > len(mat[1]):
        return math.floor(n)
    elif len(mat[0]) < len(mat[1]):
        return math.ceil(n)
    elif len(mat[0]) == len(mat[1]):
        return round(n)
