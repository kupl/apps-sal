from itertools import chain

def validSolution(board):
    cols = zip(*board)
    squares = (chain(*(board[y+i][x:x+3] for i in range(3)))
               for x in (0, 3, 6) for y in (0, 3, 6))
    good_range = set(range(1, 10))
    return all(set(zone) == good_range for zone in chain(board, cols, squares))
