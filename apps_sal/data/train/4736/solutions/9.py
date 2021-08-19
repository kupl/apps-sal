VARIANTS = ['bee', 'eeb']


def how_many_bees(hive):
    count = 0
    if hive is None:
        return count
    rl = len(hive)
    for i in range(rl):
        cl = len(hive[i])
        for j in range(0, len(hive[i])):
            print('i=', i, 'j=', j)
            o = hive[i][j]
            if j < cl - 2:
                x1 = hive[i][j + 1]
                x2 = hive[i][j + 2]
                x = o + x1 + x2
                if x in VARIANTS:
                    count += 1
            if i < rl - 2:
                y1 = hive[i + 1][j]
                y2 = hive[i + 2][j]
                y = o + y1 + y2
                if y in VARIANTS:
                    count += 1
    return count
