from numpy import matrix


def matrix_mult(a, b):
    return (matrix(a) * matrix(b)).tolist()
