import numpy as np


def round_it(n):
    return np.ceil(n) if len(str(n).split(".")[0]) < len(str(n).split(".")[1]) else np.floor(n) if len(str(n).split(".")[0]) > len(str(n).split(".")[1]) else np.round(n)
