def table_game(t):
    return [t[0][0], t[0][2], t[2][0], t[2][2]] if (t[0][1] + t[2][1]) == (t[1][0] + t[1][2]) == t[1][1] else [-1]
