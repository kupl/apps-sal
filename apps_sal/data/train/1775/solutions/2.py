import numpy as np


def duped(l):
    for e in l:
        if l.count(e) > 1:
            return True
    return False


def find_empty(city):
    for r in range(4):
        for c in range(4):
            if city[r][c] == 0:
                return (r, c)


def check_clue(clue, counter):
    if clue == 0:
        return True
    return counter == clue


def vis(arr, clues):
    l = len(arr)
    a1 = 0
    a2 = 0
    counter1 = 0
    counter2 = 0
    for k in range(l):
        if arr[k] > a1:
            a1 = arr[k]
            counter1 += 1
        if arr[l - k - 1] > a2:
            a2 = arr[l - k - 1]
            counter2 += 1
    if l < 4:
        return True
    return check_clue(clues[0], counter1) and check_clue(clues[1], counter2)


def is_valid(r, c, city, clues):
    row = [h for h in city[r] if h != 0]
    col = [r[c] for r in city if r[c] != 0]
    if duped(row) or duped(col):
        return False
    (tc, rc, bc, lc) = [clues[k][c] if k % 2 == 0 else clues[k][r] for k in range(4)]
    return vis(row, (lc, rc)) and vis(col, (tc, bc))


def solve(city, clues):
    pos = find_empty(city)
    if not pos:
        return True
    (r, c) = pos
    for n in range(1, 5):
        city[r][c] = n
        if is_valid(r, c, city, clues):
            if solve(city, clues):
                return True
        city[r][c] = 0
    return False


def solve_puzzle(clues):
    clues = [list(clues[k:k + 4]) if k < 5 else list(reversed(clues[k:k + 4])) for k in range(0, 13, 4)]
    city = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    solve(city, clues)
    return tuple([tuple(a) for a in city])
