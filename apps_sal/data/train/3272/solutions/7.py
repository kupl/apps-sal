import numpy as np


def find_average(N):
    return 0 if len(N) < 1 else np.mean(N)
