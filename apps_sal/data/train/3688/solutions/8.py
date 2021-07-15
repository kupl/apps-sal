def table_game(table):
    if table[0][1] + table[1][0] + table[1][2] + table[2][1] == table[1][1] * 2:
        if table[0][0] + table[0][2] == table[0][1]:
            if table[2][0] + table[2][2] == table[2][1]:
                if table[0][0] + table[2][0] == table[1][0]:
                    if table[0][2] + table[2][2] == table[1][2]:
                        return [table[0][0],table[0][2],table[2][0],table[2][2]]
    return [-1]
