import numpy as np
def leaderboard_climb(arr, kara):
    a = np.unique(arr)
    return list(len(a) + 1 - np.searchsorted(a, kara, side='right'))
