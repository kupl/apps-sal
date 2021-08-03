import numpy as np


def amazon_check_mate(king, amazon):
    nogo_board = np.full((24, 24), True)
    nogo_board[8:16, 8:16] = False
    king_sq = (ord(king[1]) - ord('1') + 8, ord(king[0]) - ord('a') + 8)
    nogo_board[(king_sq[0] - 1):(king_sq[0] + 2), (king_sq[1] - 1):(king_sq[1] + 2)] = True
    amazon_sq = (ord(amazon[1]) - ord('1') + 8, ord(amazon[0]) - ord('a') + 8)
    for di, dj in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        nogo_board[amazon_sq[0] + di, amazon_sq[1] + dj] = True
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    blocked = [False] * 8
    for ii in range(1, 8):
        for index, dd in enumerate(directions):
            if amazon_sq[0] + ii * dd[0] == king_sq[0] and amazon_sq[1] + ii * dd[1] == king_sq[1]:
                blocked[index] = True
            elif not blocked[index]:
                nogo_board[amazon_sq[0] + ii * dd[0], amazon_sq[1] + ii * dd[1]] = True
    if abs(king_sq[0] - amazon_sq[0]) <= 1 and abs(king_sq[1] - amazon_sq[1]) <= 1:
        nogo_board[amazon_sq[0], amazon_sq[1]] = True
    print(king_sq, amazon_sq)
    answer = [0, 0, 0, 0]
    for ii in range(8, 16):
        for jj in range(8, 16):
            if (abs(ii - king_sq[0]) > 1 or abs(jj - king_sq[1]) > 1) and\
               (ii != amazon_sq[0] or jj != amazon_sq[1]):
                if nogo_board[(ii - 1):(ii + 2), (jj - 1):(jj + 2)].all():
                    answer[0] += 1
                elif nogo_board[ii, jj]:
                    answer[1] += 1
                elif nogo_board[(ii - 1):(ii + 2), (jj - 1):(jj + 2)].sum() == 8:
                    answer[2] += 1
                else:
                    answer[3] += 1

    return answer
