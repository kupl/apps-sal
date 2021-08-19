import numpy as np


def vector_length(vector):
    (P1, P2) = map(np.array, vector)
    return np.linalg.norm(P1 - P2)
