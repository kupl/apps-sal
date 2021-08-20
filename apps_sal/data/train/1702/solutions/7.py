from itertools import chain


class Sudoku(object):

    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.nums = set(range(1, self.n + 1))

    def is_valid(self):
        return all((len(row) == self.n for row in self.data)) and self.are_all_ints() and self.are_row_nums_valid() and self.are_col_nums_valid() and self.are_squares_valid()

    def are_all_ints(self):
        return all((isinstance(x, int) and (not isinstance(x, bool)) for row in self.data for x in row))

    def are_row_nums_valid(self):
        return all((set(row) == self.nums for row in self.data))

    def are_col_nums_valid(self):
        return all((set(row) == self.nums for row in zip(*self.data)))

    def are_squares_valid(self):
        sq = int(self.n ** 0.5)
        return all((set(chain.from_iterable((row[j:j + sq] for row in self.data[i:i + sq]))) == self.nums for i in range(0, self.n, sq) for j in range(0, self.n, sq)))
