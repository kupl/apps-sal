import numpy as np
def avg_array(arrs):
    return (np.sum(arrs, 0) / len(arrs)).tolist()
