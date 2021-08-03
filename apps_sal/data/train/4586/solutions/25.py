import numpy as np


def tv_remote(word):
    keyboard = np.array([["a", "b", "c", "d", "e", "1", "2", "3"], ["f", "g", "h", "i", "j", "4", "5", "6"], ["k", "l", "m", "n", "o", "7", "8", "9"], ["p", "q", "r", "s", "t", ".", "@", "0"], ["u", "v", "w", "x", "y", "z", "_", "/"]])
    x, y = 0, 0
    moves = 0
    for i in word:
        moves += abs(np.argwhere(keyboard == i)[0][0] - y) + abs(np.argwhere(keyboard == i)[0][1] - x) + 1
        x, y = np.argwhere(keyboard == i)[0][1], np.argwhere(keyboard == i)[0][0]
    return moves
