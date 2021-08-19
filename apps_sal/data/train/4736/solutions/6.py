def how_many_bees(hive):
    counter = 0
    try:
        for row in hive:
            for i in range(len(row) - 2):
                if row[i] == 'b' and row[i + 1] == 'e' and (row[i + 2] == 'e'):
                    counter += 1
                elif row[i] == 'e' and row[i + 1] == 'e' and (row[i + 2] == 'b'):
                    counter += 1
        for column in range(len(hive[0])):
            for position in range(len(hive) - 2):
                if hive[position][column] == 'b' and hive[position + 1][column] == 'e' and (hive[position + 2][column] == 'e'):
                    counter += 1
                if hive[position][column] == 'e' and hive[position + 1][column] == 'e' and (hive[position + 2][column] == 'b'):
                    counter += 1
    except:
        counter = 0
    return counter
