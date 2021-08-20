import numpy as np


def gimme(input_array):
    return input_array.index(np.setdiff1d(input_array, [max(input_array), min(input_array)]))
