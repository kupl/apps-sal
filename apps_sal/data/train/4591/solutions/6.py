def how_many_bees(hive):
    if not hive:
        return 0
    def gather_bees(row,col):
        h = col<len(hive[row])-2 
        if h:
            yield hive[row][col]+hive[row][col+1]+hive[row][col+2]
        v = row<len(hive)-2
        if v:
            yield hive[row][col]+hive[row+1][col]+hive[row+2][col]
        if h and v:
            yield hive[row][col]+hive[row+1][col+1]+hive[row+2][col+2]
            yield hive[row+2][col]+hive[row+1][col+1]+hive[row][col+2]
    count = 0
    for row in range(len(hive)):
        for col in range(len(hive[row])):
            count += sum(1 for x in gather_bees(row,col) if x in ['bee','eeb'])
    return count
