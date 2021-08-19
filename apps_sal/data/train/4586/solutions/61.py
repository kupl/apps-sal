import numpy as np


def tv_remote(word):
    keys = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])
    [x1, y1] = [0, 0]
    totdist = 0
    for i in range(0, len(word), 1):
        [x2, y2] = np.where(keys == word[i])
        dist = abs(x1 - x2) + abs(y1 - y2)
        totdist += dist + 1
        [x1, y1] = [x2, y2]
    return totdist
