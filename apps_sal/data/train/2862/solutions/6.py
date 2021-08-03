import numpy as np


def leaderboard_climb(arr, kara):
    uniq_scores = np.unique(arr)
    l = len(uniq_scores) + 1
    t = l - np.searchsorted(uniq_scores, kara, side='right')
    return t.tolist()
