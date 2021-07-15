import numpy as np
def find_difference(a, b):
    return np.prod(a)-np.prod(b) if np.prod(a)>np.prod(b) else np.prod(b)-np.prod(a)
