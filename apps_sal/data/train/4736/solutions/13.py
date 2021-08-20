def how_many_bees(hive):
    bees = ('bee', 'eeb')
    num_of_bees = 0
    if hive == None:
        return 0
    for line in hive:
        for pos in range(len(line) - 2):
            possible_bee = line[pos] + line[pos + 1] + line[pos + 2]
            if possible_bee in bees:
                num_of_bees += 1
    for line_idx in range(len(hive) - 2):
        for pos_idx in range(len(hive[line_idx])):
            possible_bee = hive[line_idx][pos_idx] + hive[line_idx + 1][pos_idx] + hive[line_idx + 2][pos_idx]
            if possible_bee in bees:
                num_of_bees += 1
    return num_of_bees
