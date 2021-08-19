import numpy as np


def tv_remote(word):
    answer = 0
    remote = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'], ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])
    row = 0
    col = 0
    for i in word:
        current_pos = np.where(remote == i)
        answer += abs(row - current_pos[0][0]) + abs(col - current_pos[1][0])
        row = current_pos[0][0]
        col = current_pos[1][0]
    answer += len(word)
    return answer
