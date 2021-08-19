def how_many_bees(hive):
    if not hive:
        return 0
    count = 0
    for i in range(len(hive)):
        for j in range(len(hive[i]) - 2):
            compare = ''.join(hive[i][j:j + 3])
            if compare == 'bee' or compare == 'eeb':
                count += 1
    for i in range(len(hive) - 2):
        for j in range(len(hive[i])):
            compare = hive[i][j] + hive[i + 1][j] + hive[i + 2][j]
            if compare == 'bee' or compare == 'eeb':
                count += 1
    return count
