from scipy.ndimage.morphology import binary_erosion as erode, numpy as np

def peak_height(mountain):
    M, n = np.array([*map(list,mountain)]) == "^", 0
    while M.any(): M, n = erode(M), n+1
    return n
