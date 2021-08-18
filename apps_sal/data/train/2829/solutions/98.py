import numpy as np


def array_madness(a, b):
    a, b = np.array(a), np.array(b)
    squaring_array1 = a ** 2
    cube_array2 = b ** 3
    if sum(squaring_array1) > sum(cube_array2):
        return True
    else:
        return False
