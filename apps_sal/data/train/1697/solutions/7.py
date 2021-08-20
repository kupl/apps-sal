from itertools import permutations


class Nonogram:

    def __init__(self, clues):
        self.cols = clues[0]
        self.rows = clues[1]
        self.dim = len(self.cols)
        self.field = [[' ' for j in range(self.dim)] for i in range(self.dim)]
        self.rows_p = [None] * self.dim
        self.cols_p = [None] * self.dim

    def __str__(self):
        max_hint_length = (self.dim + 1) // 2
        rows = []
        for i in range(max_hint_length):
            row = [' ' if len(self.cols[d]) + i < max_hint_length else str(self.cols[d][len(self.cols[d]) - max_hint_length + i]) for d in range(self.dim)]
            rows.append(' ' * max_hint_length + '|' + ''.join(row))
        rows.append('-' * max_hint_length + '+' + '-' * self.dim)
        for i in range(self.dim):
            row = [' ' if len(self.rows[i]) + j < max_hint_length else str(self.rows[i][len(self.rows[i]) - max_hint_length + j]) for j in range(max_hint_length)]
            row_field = [str(self.field[i][d]) for d in range(self.dim)]
            rows.append(''.join(row) + '|' + ''.join(row_field))
        return '\n'.join(rows)

    def possibilities(self, clues, sure=None):
        poss = [''.join(pp) for pp in set(permutations('0' * len(clues) + '.' * (self.dim - sum(clues)))) if '00' not in ''.join(pp)]
        for x in range(len(poss)):
            for num in clues:
                poss[x] = poss[x].replace('0', 'X' * num, 1)
        if sure is not None:
            poss = list([p for p in poss if all([sure[d] == ' ' or sure[d] == p[d] for d in range(self.dim)])])
        return poss

    def sure(self, poss):
        return ''.join(['X' if all([p[d] == 'X' for p in poss]) else '.' if all([p[d] == '.' for p in poss]) else ' ' for d in range(self.dim)])

    def update_rows_p(self, i, j, s):
        if self.rows_p[i] is not None:
            self.rows_p[i] = list([poss for poss in self.rows_p[i] if poss[j] == s])
            sure = self.sure(self.rows_p[i])
            if not sure.isspace():
                self.update_field(sure, i=i)

    def update_cols_p(self, i, j, s):
        if self.cols_p[j] is not None:
            self.cols_p[j] = list([poss for poss in self.cols_p[j] if poss[i] == s])
            sure = self.sure(self.cols_p[j])
            if not sure.isspace():
                self.update_field(sure, j=j)

    def update_field(self, sure, i=None, j=None):
        if i is not None:
            for j in range(self.dim):
                if sure[j] in ('X', '.') and self.field[i][j] == ' ':
                    self.field[i][j] = sure[j]
                    self.update_cols_p(i, j, sure[j])
        elif j is not None:
            for i in range(self.dim):
                if sure[i] in ('X', '.') and self.field[i][j] == ' ':
                    self.field[i][j] = sure[i]
                    self.update_rows_p(i, j, sure[i])

    def solve(self):
        for i in range(self.dim):
            poss = self.possibilities(clues=self.rows[i])
            self.rows_p[i] = poss
            sure = self.sure(poss=poss)
            if not sure.isspace():
                self.update_field(sure, i=i)
        for j in range(self.dim):
            poss = self.possibilities(clues=self.cols[j], sure=[self.field[i][j] for i in range(self.dim)])
            self.cols_p[j] = poss
            sure = self.sure(poss=poss)
            if not sure.isspace():
                self.update_field(sure, j=j)
        return tuple((tuple((0 if c == '.' else 1 for c in r)) for r in self.field))
