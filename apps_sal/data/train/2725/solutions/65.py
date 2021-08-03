import numpy as np


def gimme(input_array):
    choices = set([0, 1, 2])
    not_it = set([np.argmin(input_array), np.argmax(input_array)])
    return list(choices - not_it)[0]
