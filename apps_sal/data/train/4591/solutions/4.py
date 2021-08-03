def how_many_bees(hive):
    if type(hive) != list:
        return 0
    n = 0
    l = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x in range(len(hive)):
        for y in range(len(hive[x])):
            if hive[x][y] == 'b':
                for i in l:
                    if 0 <= x + i[0] * 2 < len(hive) and 0 <= y + i[1] * 2 < len(hive[x]) and hive[x + i[0]][y + i[1]] == 'e' and hive[x + i[0] * 2][y + i[1] * 2] == 'e':
                        n += 1
    return n
