import numpy as np


def mean_vs_median(numbers):
    mean_v = np.mean(numbers)
    median_v = np.median(numbers)
    if mean_v < median_v:
        return 'median'
    elif mean_v > median_v:
        return 'mean'
    else:
        return 'same'
