import numpy as np

def poly_multiply(p1, p2):
    return np.trim_zeros(np.polymul(p1, p2), 'f').tolist()
