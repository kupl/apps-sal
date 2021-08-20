def table_game(t):
    [a, b, c, d] = [t[0][0], t[0][2], t[2][0], t[2][2]]
    return [a, b, c, d] if t[0][1] == a + b and t[1][0] == a + c and (t[1][2] == b + d) and (t[1][1] == a + b + c + d) and (t[2][1] == c + d) else [-1]
