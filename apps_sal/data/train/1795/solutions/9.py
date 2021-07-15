from copy import deepcopy

def nQueen(size):
    for y in range((size+1)//2):
        board = tuple(set(range(size)) for _ in range(size))
        if solve(board, set(), size, 0, y):
            return [s.pop() for s in board]
    return []

def solve(board, placed, size, sx, sy):
    board[sx].intersection_update({sy})
    placed.add(sx)
    for x in range(size):
        if x == sx: continue
        board[x].difference_update({sy, sy+sx-x, sy+x-sx})
        if not board[x]: return False
    if len(placed) == size: return True
    min_v = size
    min_x = None
    for x in range(size):
        if x in placed: continue
        lx = len(board[x])
        if lx == 1: return solve(board, placed, size, x, next(iter(board[x])))
        if lx < min_v:
            min_v = lx
            min_x = x
    for y in board[min_x]:
        new_board = deepcopy(board)
        new_placed = placed.copy()
        if solve(new_board, new_placed, size, min_x, y):
            update(board, new_board)
            return True
    return False

def update(board, new_board):
    for s, ns in zip(board, new_board):
        s.clear()
        s.update(ns)


