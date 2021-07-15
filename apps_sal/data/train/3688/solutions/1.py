def table_game(table):
    a, b, c, d = table[0][0], table[0][2], table[2][0], table[2][2]
    guess = [[a, a + b, b], [a + c, a + b + c + d, b + d], [c, c + d, d]]
    return [a, b, c, d] if table == guess else [-1]
