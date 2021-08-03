import numpy as np


def find_word(board, word, seen=[]):
    board = np.array(board)
    inds = np.argwhere(board == word[0])
    if seen:
        inds = inds[[list(ind) not in seen for ind in inds]]
        last = seen[-1]
        inds = inds[[max(row) == 1 for row in abs(inds - last)]]

    if len(word) == 1:
        return len(inds) > 0
    return any(find_word(board, word[1:], seen=seen + [list(ind)]) for ind in inds)
