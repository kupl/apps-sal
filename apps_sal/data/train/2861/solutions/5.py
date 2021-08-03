import numpy as np

# Will work in any dimension


def vector_length(vector):
    P1, P2 = map(np.array, vector)
    return np.linalg.norm(P1 - P2)
