class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = -1

    def insert(self, zero, n, row: List[int], i: int, counts: List[int]) -> int:
        if len(row) == n:
            if self.data == -1:
                self.data = i
                counts[self.data] = 1 + counts[i]
                return i + 1
            else:
                counts[self.data] += 1
                return i
        elif row[n] == zero:
            if self.left is None:
                self.left = Tree()
            return self.left.insert(zero, n + 1, row, i, counts)
        else:  # row[1] == one
            if self.right is None:
                self.right = Tree()
            return self.right.insert(zero, n + 1, row, i, counts)


class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        firstcell = matrix[0][0]
        vals = Tree()
        counts = [0] * 300
        nextfree = 0

        for row in matrix:
            firstrowcell = row[0]
            nextfree = vals.insert(firstcell if firstrowcell == 0 else 1 - firstcell, 0, row, nextfree, counts)

        return max(counts)
