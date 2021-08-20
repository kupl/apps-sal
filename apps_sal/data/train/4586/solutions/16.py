import numpy as np


def tv_remote(word):
    table = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])
    cur = [0, 0]
    result = 0
    for char in word:
        new = np.argwhere(char == table)
        result += 1 + sum(abs(new - cur).flat)
        cur = new
    return result
