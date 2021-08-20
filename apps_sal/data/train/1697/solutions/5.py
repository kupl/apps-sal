from itertools import permutations


def count_blacks(list):
    count = 0
    chain = False
    blacks = []
    for i in list:
        if i == 1:
            if chain == False:
                chain = True
                count += 1
            else:
                count += 1
        if i != 1:
            if chain == False:
                continue
            else:
                blacks.append(count)
                count = 0
                chain = False
    if chain == True:
        blacks.append(count)
    return tuple(blacks)


class Row:

    def __init__(self, nrow, length, blacks):
        self.nrow = nrow
        self.length = length
        self.blacks = blacks
        self.combs = []
        if len(self.blacks) == 1 and self.blacks[0] > 0:
            for i in range(self.length - self.blacks[0] + 1):
                self.combs.append([0 for i in range(i)] + [1 for j in range(self.blacks[0])] + [0 for k in range(self.length - (i + self.blacks[0]))])
        elif len(self.blacks) > 1:
            self.totalblacks = 0
            for i in self.blacks:
                self.totalblacks += i
            self.blanks = self.length - self.totalblacks
            self.items = []
            for i in range(self.blanks):
                self.items.append(0)
            for i in range(self.totalblacks):
                self.items.append(1)
            for p in permutations(self.items):
                if p not in self.combs and count_blacks(p) == self.blacks:
                    self.combs.append(p)

    def __str__(self):
        return str(self.nrow) + ',' + str(self.length) + ',' + str(self.blacks)


class Col:

    def __init__(self, ncol, length, blacks):
        self.ncol = ncol
        self.length = length
        self.blacks = blacks
        self.combs = []
        if len(self.blacks) == 1 and self.blacks[0] > 0:
            for i in range(self.length - self.blacks[0] + 1):
                self.combs.append([0 for i in range(i)] + [1 for j in range(self.blacks[0])] + [0 for k in range(self.length - (i + self.blacks[0]))])
        elif len(self.blacks) > 1:
            self.totalblacks = 0
            for i in self.blacks:
                self.totalblacks += i
            self.blanks = self.length - self.totalblacks
            self.items = []
            for i in range(self.blanks):
                self.items.append(0)
            for i in range(self.totalblacks):
                self.items.append(1)
            for p in permutations(self.items):
                if p not in self.combs and count_blacks(p) == self.blacks:
                    self.combs.append(p)

    def __str__(self):
        return str(self.ncol) + ',' + str(self.length) + ',' + str(self.blacks)


class Nonogram:

    def __init__(self, clues):
        self.nrows = len(clues[1])
        self.ncols = len(clues[0])
        self.board = [[0 for i in range(self.ncols)] for j in range(self.nrows)]
        self.rclues = clues[1]
        self.cclues = clues[0]
        self.rows = []
        self.cols = []
        for i in range(self.nrows):
            self.rows.append(Row(i, self.ncols, self.rclues[i]))
        for j in range(self.ncols):
            self.cols.append(Col(j, self.nrows, self.cclues[j]))

    def solve(self):
        self.solved = False
        while self.solved == False:
            for row in self.rows:
                if len(row.combs) > 0:
                    for c in range(row.length):
                        self.check = []
                        for r in row.combs:
                            self.check.append(r[c] == 1)
                        if all(self.check):
                            self.board[row.nrow][c] = 1
                            self.crosscheck = []
                            for i in self.cols[c].combs:
                                if i[row.nrow] != 1:
                                    self.crosscheck.append(i)
                            for d in self.crosscheck:
                                self.cols[c].combs.remove(d)
            for row in self.rows:
                if len(row.combs) > 0:
                    for c in range(row.length):
                        self.check = []
                        for r in row.combs:
                            self.check.append(r[c] == 0)
                        if all(self.check):
                            self.crosscheck = []
                            for i in self.cols[c].combs:
                                if i[row.nrow] != 0:
                                    self.crosscheck.append(i)
                            for d in self.crosscheck:
                                self.cols[c].combs.remove(d)
            for col in self.cols:
                if len(col.combs) > 0:
                    for c in range(col.length):
                        self.check = []
                        for r in col.combs:
                            self.check.append(r[c] == 1)
                        if all(self.check):
                            self.board[c][col.ncol] = 1
                            self.crosscheck = []
                            for i in self.rows[c].combs:
                                if i[col.ncol] != 1:
                                    self.crosscheck.append(i)
                            for d in self.crosscheck:
                                self.rows[c].combs.remove(d)
            for col in self.cols:
                if len(col.combs) > 0:
                    for c in range(col.length):
                        self.check = []
                        for r in col.combs:
                            self.check.append(r[c] == 0)
                        if all(self.check):
                            self.crosscheck = []
                            for i in self.rows[c].combs:
                                if i[col.ncol] != 0:
                                    self.crosscheck.append(i)
                            for d in self.crosscheck:
                                self.rows[c].combs.remove(d)
            self.checksolutions = []
            for r in range(self.nrows):
                self.checksolutions.append(count_blacks(self.board[r]) == self.rclues[r])
            for c in range(self.ncols):
                self.transposedboard = [[self.board[j][i] for j in range(self.ncols)] for i in range(self.nrows)]
                self.checksolutions.append(count_blacks(self.transposedboard[c]) == self.cclues[c])
            if all(self.checksolutions):
                self.solved = True
                self.solution = []
        for r in self.board:
            self.solution.append(tuple(r))
        return tuple(self.solution)
