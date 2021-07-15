def how_many_bees(hive):
    if not(hive) or not(len(hive)) or not(len(hive[0])):
        return 0
    class Model(object):
        def __init__(self):
            self.bees = 0
        def checker(self, row, col):
            if row > 1 and hive[row - 1][col] == 'e' and hive[row - 2][col] == 'e':
                self.bees += 1
            if row < len(hive) - 2 and hive[row + 1][col] == 'e' and hive[row + 2][col] == 'e':
                self.bees += 1
            if col > 1 and hive[row][col - 1] == 'e' and hive[row][col - 2] == 'e':
                self.bees += 1
            if col < len(hive[0]) - 2 and hive[row][col + 1] == 'e' and hive[row][col + 2] == 'e':
                self.bees += 1
            if row > 1 and col > 1 and hive[row - 1][col - 1] == 'e' and hive[row - 2][col - 2] == 'e':
                self.bees += 1
            if row < len(hive) - 2 and col > 1 and hive[row + 1][col - 1] == 'e' and hive[row + 2][col - 2] == 'e':
                self.bees += 1
            if row > 1 and col < len(hive[0]) - 2 and hive[row - 1][col + 1] == 'e' and hive[row - 2][col + 2] == 'e':
                self.bees += 1
            if row < len(hive) - 2 and col < len(hive[0]) - 2 and hive[row + 1][col + 1] == 'e' and hive[row + 2][col + 2] == 'e':
                self.bees += 1
    b = Model()
    for i in range(len(hive)):
        for j in range(len(hive[i])):
            if hive[i][j] == 'b':
                b.checker(i, j)
    return b.bees
