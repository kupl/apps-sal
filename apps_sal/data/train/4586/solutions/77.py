import numpy as np


def tv_remote(word):
    keyboard = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
                         ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
                         ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
                         ['p', 'q', 'r', 's', 't', '.', '@', '0'],
                         ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])
    x1, y1, sum = 0, 0, 0
    for letter in word:
        x2, y2 = np.argwhere(keyboard == letter)[0][:]
        sum += 1 + abs(x2 - x1) + abs(y2 - y1)
        x1, y1 = x2, y2
    return sum
