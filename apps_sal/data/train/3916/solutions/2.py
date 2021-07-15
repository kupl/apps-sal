import numpy as np

def mean_vs_median(numbers):
    return {-1: "median", 0: "same", 1: "mean"}.get (np.sign(np.mean(numbers) - np.median(numbers)))

