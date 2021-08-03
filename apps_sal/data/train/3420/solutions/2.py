import numpy as np


def absolute_values_sum_minimization(A):
    return np.median(A) if len(A) % 2 else A[len(A) // 2 - 1]
