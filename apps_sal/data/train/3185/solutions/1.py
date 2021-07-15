import numpy as np

def rotate_against_clockwise(matrix, times):
    return np.rot90(matrix, times).tolist()
