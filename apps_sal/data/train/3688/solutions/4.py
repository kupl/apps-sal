def table_game(table):
    return [table[i][j] for i in (0, 2) for j in (0, 2)] if all((table[0][i] + table[2][i] == table[1][i] and table[i][0] + table[i][2] == table[i][1] for i in range(3))) else [-1]
