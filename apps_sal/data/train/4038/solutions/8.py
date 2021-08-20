def chess_knight(pos):
    (i, j) = (int(8 - int(pos[1])), 'abcdefgh'.index(pos[0]))
    (A, B, C, D, E, F, G, H) = (i > 0, i < 7, j - 2 >= 0, j + 2 < 8, i + 2 < 8, i - 2 >= 0, j > 0, j < 7)
    return sum([A and D, A and C, B and C, B and D, F and H, F and G, E and H, E and G])
