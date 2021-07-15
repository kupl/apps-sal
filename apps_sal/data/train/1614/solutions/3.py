import numpy as np
from scipy.signal import convolve2d
def who_is_winner(pieces_position_list):
    arr = np.zeros((7,6), int)
    for a in pieces_position_list:
        pos, color = a.split('_')
        pos = ord(pos) - ord('A')
        val = (-1,1)[color == 'Red']
        arr[pos, np.argmin(arr[pos] != 0)] = val
        t_arr = val * arr
        if any(np.max(cv) == 4 for cv in (convolve2d(t_arr, [[1,1,1,1]], 'same'),
                                          convolve2d(t_arr, [[1],[1],[1],[1]], 'same'),
                                          convolve2d(t_arr, [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]], 'same'),
                                          convolve2d(t_arr, [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]], 'same'))):
            return color
    return 'Draw'
